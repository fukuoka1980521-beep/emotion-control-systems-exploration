import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent / "generated"
OUT.mkdir(exist_ok=True)
SEED = 20260916 + 81
rng_master = np.random.default_rng(SEED)

N_AGENTS = 1500
T = 120
ATTACHMENT = 1.0
ACTIONS = ["wait", "inspect", "protect", "escape"]

def threat_schedule(t):
    if 30 <= t < 50:
        return 0.85
    if 80 <= t < 90:
        return 0.45
    return 0.0

def action_cost(action, fatigue):
    base = {"wait":0.00, "inspect":0.05, "protect":0.13, "escape":0.11}[action]
    effort = {"wait":0.00, "inspect":0.20, "protect":0.90, "escape":0.70}[action]
    return base + fatigue * effort * 0.20

def policy_utilities(threat, memory, arousal, fatigue, pain, body_feedback=True):
    perceived = threat + 0.42 * memory
    if body_feedback:
        protect_gain = ATTACHMENT * perceived * (0.72 + 0.58 * arousal)
        escape_gain = perceived * (0.55 + 0.72 * arousal + 0.70 * pain)
        temp = max(0.16, 0.44 - 0.18 * arousal)
        f = fatigue
    else:
        protect_gain = ATTACHMENT * perceived * 0.82
        escape_gain = perceived * 0.72
        temp = 0.40
        f = 0.0
    inspect_gain = 0.24 * (1.0 - perceived) + 0.16 * perceived
    wait_gain = 0.22 * (1.0 - perceived)
    u = {
        "wait": wait_gain - action_cost("wait", f),
        "inspect": inspect_gain - action_cost("inspect", f),
        "protect": protect_gain - action_cost("protect", f),
        "escape": escape_gain - action_cost("escape", f),
    }
    return u, temp

def probs_from_u(u, temp):
    keys = list(u)
    x = np.array([u[k] for k in keys], dtype=float)
    x -= x.max()
    p = np.exp(x / temp)
    p /= p.sum()
    return keys, p

def run_agent(condition, seed):
    rng = np.random.default_rng(seed)
    arousal = 0.15
    fatigue = 0.05
    pain = 0.0
    memory = 0.0
    rows = []
    for t in range(T):
        threat = threat_schedule(t)
        body_feedback = condition != "no_body_feedback"
        use_memory = condition != "body_without_memory"
        effective_memory = memory if use_memory else 0.0
        u, temp = policy_utilities(threat, effective_memory, arousal, fatigue, pain, body_feedback)
        keys, p = probs_from_u(u, temp)
        action = rng.choice(keys, p=p)
        if action == "protect":
            damage_p = max(0.0, threat * 0.12)
        elif action == "escape":
            damage_p = max(0.0, threat * 0.18)
        elif action == "inspect":
            damage_p = max(0.0, threat * 0.42)
        else:
            damage_p = max(0.0, threat * 0.55)
        damaged = int(rng.random() < damage_p)
        arousal = np.clip(
            0.82 * arousal
            + 0.30 * threat
            + 0.28 * damaged
            + (0.07 if action in ("protect","escape") else 0.0),
            0.0, 1.0
        )
        fatigue = np.clip(
            0.965 * fatigue
            + {"wait":0.00,"inspect":0.018,"protect":0.055,"escape":0.040}[action],
            0.0, 1.0
        )
        pain = np.clip(0.90 * pain + 0.55 * damaged, 0.0, 1.0)
        memory = np.clip(0.88 * memory + 0.26 * threat + 0.22 * damaged, 0.0, 1.0)
        entropy = float(-(p * np.log(p + 1e-12)).sum())
        rows.append({
            "condition": condition,
            "t": t,
            "threat": threat,
            "action": action,
            "defensive": int(action in ("protect","escape")),
            "protect": int(action=="protect"),
            "escape": int(action=="escape"),
            "damaged": damaged,
            "arousal": arousal,
            "fatigue": fatigue,
            "pain": pain,
            "memory": memory,
            "entropy": entropy,
        })
    return pd.DataFrame(rows)

conditions = ["closed_loop_body", "no_body_feedback", "body_without_memory"]
seeds = rng_master.integers(0, 2**32-1, size=N_AGENTS * len(conditions))
si = 0
runs = []
for c in conditions:
    for agent in range(N_AGENTS):
        d = run_agent(c, int(seeds[si]))
        si += 1
        d["agent"] = agent
        runs.append(d)

df = pd.concat(runs, ignore_index=True)

ts = (
    df.groupby(["condition","t"], as_index=False)
      .agg(
          defensive_rate=("defensive","mean"),
          protect_rate=("protect","mean"),
          escape_rate=("escape","mean"),
          damage_rate=("damaged","mean"),
          mean_arousal=("arousal","mean"),
          mean_fatigue=("fatigue","mean"),
          mean_pain=("pain","mean"),
          mean_memory=("memory","mean"),
          mean_entropy=("entropy","mean"),
      )
)

metrics = []
for c in conditions:
    d = df[df.condition==c]
    w1 = d[(d.t>=30)&(d.t<50)]
    rec1 = d[(d.t>=50)&(d.t<70)]
    w2 = d[(d.t>=80)&(d.t<90)]
    rec2 = d[(d.t>=90)&(d.t<110)]
    metrics.append({
        "condition": c,
        "first_threat_defensive_rate": w1.defensive.mean(),
        "first_threat_damage_rate": w1.damaged.mean(),
        "post_first_threat_defensive_rate": rec1.defensive.mean(),
        "second_weaker_threat_defensive_rate": w2.defensive.mean(),
        "second_weaker_threat_damage_rate": w2.damaged.mean(),
        "post_second_threat_defensive_rate": rec2.defensive.mean(),
        "mean_arousal_second_threat": w2.arousal.mean(),
        "mean_fatigue_second_threat": w2.fatigue.mean(),
        "mean_pain_second_threat": w2.pain.mean(),
        "mean_entropy_second_threat": w2.entropy.mean(),
    })
metrics_df = pd.DataFrame(metrics)
metrics_df["history_amplification_index"] = (
    metrics_df["second_weaker_threat_defensive_rate"]
    - metrics_df["post_first_threat_defensive_rate"]
)

metrics_df.to_csv(OUT/"attachment_emotion_v8_1_closed_loop_metrics.csv",index=False)
ts.to_csv(OUT/"attachment_emotion_v8_1_closed_loop_timeseries.csv",index=False)
