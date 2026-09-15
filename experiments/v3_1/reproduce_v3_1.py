"""Reconstruction of V3.1 from preserved V3 utility outputs and the V3.1 correction record.

Important: this is not claimed to be the original source file. The linear utility
coefficients below were reconstructed from the full-precision utility values saved
in the V3 action-rate archive. V3.1's documented correction removes actor-directed
actions from the natural-obstruction condition. With seed 20260946, the regenerated
20 x 7 summary matches the preserved V3.1 summary exactly.
"""

import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent / "generated"
OUT.mkdir(exist_ok=True)

SEED = 20260946
N = 8000
TEMP = 0.22
ATTACHMENTS = [0.0, 0.25, 0.5, 0.75, 1.0]
SCENARIOS = [
    "natural_obstruction",
    "accidental_actor",
    "intentional_justified",
    "intentional_unjustified",
]
ACTIONS = ["wait", "clear", "reroute", "confront", "sanction"]

# utility(A) = slope * A + intercept
COEFFS = {
    "natural_obstruction": {
        "wait": (0.4952159674837238, 0.0),
        "clear": (1.375215967483724, -0.12),
        "reroute": (1.1352159674837239, -0.09),
        "confront": (0.9152159674837237, -0.18),
        "sanction": (0.7952159674837238, -0.28),
    },
    "accidental_actor": {
        "wait": (0.7513621575615119, 0.0),
        "clear": (1.631362157561512, -0.12),
        "reroute": (1.3922458619172802, -0.09),
        "confront": (1.182555746067911, -0.3419999999999999),
        "sanction": (1.069625380914058, -0.628),
    },
    "intentional_justified": {
        "wait": (0.3586046661089034, 0.0),
        "clear": (1.2386046661089036, -0.12),
        "reroute": (1.012904027169996, -0.09),
        "confront": (0.9597299062160753, -0.609),
        "sanction": (0.954124794704816, -1.1990000000000005),
    },
    "intentional_unjustified": {
        "wait": (0.1878405393903779, 0.0),
        "clear": (1.067840539390378, -0.12),
        "reroute": (0.8470707146104679, -0.09),
        "confront": (0.8514227588448507, -0.018),
        "sanction": (0.8852641606055699, -0.052),
    },
}


def softmax(vals, temp=TEMP):
    vals = np.asarray(vals, float)
    vals = vals - vals.max()
    p = np.exp(vals / temp)
    return p / p.sum()


rng = np.random.default_rng(SEED)
rows = []

for attachment in ATTACHMENTS:
    for scenario in SCENARIOS:
        valid_actions = ACTIONS[:3] if scenario == "natural_obstruction" else ACTIONS
        utilities = [
            COEFFS[scenario][action][0] * attachment + COEFFS[scenario][action][1]
            for action in valid_actions
        ]
        probabilities = softmax(utilities)
        draws = rng.choice(valid_actions, size=N, p=probabilities)

        wait = np.mean(draws == "wait")
        clear = np.mean(draws == "clear")
        reroute = np.mean(draws == "reroute")
        confront = np.mean(draws == "confront") if "confront" in valid_actions else 0.0
        sanction = np.mean(draws == "sanction") if "sanction" in valid_actions else 0.0

        rows.append(
            {
                "attachment": attachment,
                "scenario": scenario,
                "goal_repair_rate": clear + reroute,
                "actor_directed_rate": confront + sanction,
                "confront_rate": confront,
                "sanction_rate": sanction,
                "wait_rate": wait,
            }
        )

pd.DataFrame(rows).to_csv(
    OUT / "attachment_anger_v3_1_corrected_summary.csv", index=False
)
