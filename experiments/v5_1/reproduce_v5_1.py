import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent / "generated"
OUT.mkdir(exist_ok=True)
SEED = 20260915 + 51
rng_master = np.random.default_rng(SEED)

ACTIONS = ["wait", "clear", "reroute", "confront", "sanction"]
COST = {"wait": 0.00, "clear": 0.10, "reroute": 0.12, "confront": 0.18, "sanction": 0.28}
ATTACHMENT = 1.0

MEMORY_REGIMES = {"cumulative": None, "slow_update": 0.02, "fast_update": 0.15}
REFORM_TYPES = ["neutral_reform", "active_amends"]

N_AGENTS = 180
HARM_STEPS = 700
REFORM_STEPS = 500
CHECKPOINTS = [0, 10, 20, 50, 100, 200, 350, 500]

Q_PRIOR = {a: -COST[a] for a in ACTIONS}

def harm_reward(action, rng):
    restore_p = {"wait":0.05,"clear":0.78,"reroute":0.67,"confront":0.48,"sanction":0.36}[action]
    next_block_p = {"wait":0.92,"clear":0.90,"reroute":0.82,"confront":0.34,"sanction":0.16}[action]
    access = int(rng.random() < restore_p)
    next_block = int(rng.random() < next_block_p)
    return ATTACHMENT * (1.20*access - 1.05*next_block) - COST[action]

def reform_reward(action, reform_type, rng):
    if reform_type == "neutral_reform":
        access_p = {"wait":0.92,"clear":0.90,"reroute":0.88,"confront":0.82,"sanction":0.78}[action]
        next_block_p = 0.04
    else:
        access_p = {"wait":0.99,"clear":0.97,"reroute":0.95,"confront":0.76,"sanction":0.66}[action]
        next_block_p = 0.01
    access = int(rng.random() < access_p)
    next_block = int(rng.random() < next_block_p)
    return ATTACHMENT * (1.20*access - 1.05*next_block) - COST[action]

def update(q, n, a, r, alpha_fixed):
    n[a] += 1
    alpha = 1/n[a] if alpha_fixed is None else alpha_fixed
    q[a] += alpha * (r - q[a])

def choose(q, rng, eps):
    if rng.random() < eps:
        return rng.choice(ACTIONS)
    mx = max(q.values())
    best = [a for a,v in q.items() if abs(v-mx) < 1e-12]
    return rng.choice(best)

def run(memory, reform, probe, seed):
    rng = np.random.default_rng(seed)
    alpha_fixed = MEMORY_REGIMES[memory]
    q = dict(Q_PRIOR)
    n = {a:0 for a in ACTIONS}
    for _ in range(HARM_STEPS):
        a = choose(q, rng, 0.06)
        update(q, n, a, harm_reward(a, rng), alpha_fixed)
    rows = []
    def snap(step):
        best = max(q, key=q.get)
        return (step, int(best in ("confront","sanction")), best)
    rows.append(snap(0))
    for step in range(1, REFORM_STEPS+1):
        if probe:
            eps = 0.35 if step <= 120 else (0.15 if step <= 250 else 0.06)
        else:
            eps = 0.05
        a = choose(q, rng, eps)
        update(q, n, a, reform_reward(a, reform, rng), alpha_fixed)
        if step in CHECKPOINTS:
            rows.append(snap(step))
    return rows

seeds = rng_master.integers(0,2**32-1,size=N_AGENTS*len(MEMORY_REGIMES)*len(REFORM_TYPES)*2)
si=0
rows=[]
for memory in MEMORY_REGIMES:
    for reform in REFORM_TYPES:
        for probe in [False,True]:
            for agent in range(N_AGENTS):
                recs=run(memory,reform,probe,int(seeds[si])); si+=1
                for step,ad,best in recs:
                    rows.append([memory,reform,probe,agent,step,ad,best])

df=pd.DataFrame(rows,columns=["memory_regime","reform_type","probe_exploration","agent","step","actor_directed","best_action"])
curve=(df.groupby(["memory_regime","reform_type","probe_exploration","step"],as_index=False)
       .agg(actor_directed_rate=("actor_directed","mean")))

metrics=[]
for memory in MEMORY_REGIMES:
    for reform in REFORM_TYPES:
        for probe in [False,True]:
            d=curve[(curve.memory_regime==memory)&(curve.reform_type==reform)&(curve.probe_exploration==probe)].sort_values("step")
            below=d[d.actor_directed_rate<=.10]
            t10=int(below.step.iloc[0]) if len(below) else None
            auc=float(np.trapezoid(d.actor_directed_rate,d.step))
            metrics.append({
                "memory_regime":memory,
                "reform_type":reform,
                "probe_exploration":probe,
                "initial":float(d.iloc[0].actor_directed_rate),
                "at_100":float(d[d.step==100].actor_directed_rate.iloc[0]),
                "at_500":float(d[d.step==500].actor_directed_rate.iloc[0]),
                "first_below_10pct":t10,
                "auc":auc,
            })
metrics=pd.DataFrame(metrics)
curve.to_csv(OUT/"attachment_emotion_v5_1_curve.csv",index=False)
metrics.to_csv(OUT/"attachment_emotion_v5_1_metrics.csv",index=False)
