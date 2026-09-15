import numpy as np
import pandas as pd

# Minimal "attachment -> emotion-like behavior" experiment.
# The agent does NOT contain variables named fear, grief, joy, etc.
# It only has generic target value, learned bond, return belief, and action selection.
# Emotion-like patterns are interpreted after the simulation.

T = 120

def softmax_choice(utilities, rng, temp=0.33):
    keys = list(utilities.keys())
    vals = np.array([utilities[k] for k in keys], dtype=float)
    vals -= vals.max()
    probs = np.exp(vals / temp)
    probs /= probs.sum()
    return rng.choice(keys, p=probs)

def run_agent(condition="full_attachment", seed=1):
    rng = np.random.default_rng(seed)
    bond = 0.0
    return_belief = 0.0
    prev_appraisal = None
    rows = []

    for t in range(T):
        present = (t < 70) or (t >= 100)
        threat = 0.10 + 0.80 * ((t - 50) / 19.0) if 50 <= t < 70 else 0.0

        if t == 70:
            return_belief = 0.90
        elif not present:
            return_belief = max(0.02, return_belief * 0.94)
        else:
            return_belief = 1.0

        effective_bond = 0.0 if condition == "value_only" else bond

        if present:
            utilities = {
                "interact": 0.95 + 0.55 * effective_bond,
                "protect": -0.20 + threat * (1.00 + 2.60 * effective_bond),
                "search": -1.00,
                "explore": 0.32,
            }
        else:
            utilities = {
                "interact": -1.00,
                "protect": -0.70,
                "search": -0.12 + return_belief * (0.35 + 3.00 * effective_bond),
                "explore": 0.32,
            }

        action = softmax_choice(utilities, rng)

        appraisal = (
            1.0 + 2.0 * effective_bond
            if present
            else return_belief * (0.35 + 2.0 * effective_bond)
        )
        prediction_error = np.nan if prev_appraisal is None else appraisal - prev_appraisal
        prev_appraisal = appraisal

        if condition == "full_attachment":
            if present and action == "interact":
                bond += 0.055 * (1.0 - bond)
            elif not present:
                bond *= 0.997
        elif condition == "short_memory":
            if present and action == "interact":
                bond += 0.055 * (1.0 - bond)
            elif not present:
                bond *= 0.82
        else:
            bond = 0.0

        bond = float(np.clip(bond, 0, 1))
        rows.append([t, condition, present, threat, bond, return_belief, action, appraisal, prediction_error])

    return pd.DataFrame(rows, columns=[
        "t","condition","present","threat","bond","return_belief","action","appraisal","prediction_error"
    ])

if __name__ == "__main__":
    for c in ["value_only","short_memory","full_attachment"]:
        print(c)
        print(run_agent(c, seed=42).tail(15))
