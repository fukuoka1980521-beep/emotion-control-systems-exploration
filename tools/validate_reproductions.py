from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    (
        "V3.1",
        ROOT / "experiments/v3_1/reproduce_v3_1.py",
        ROOT / "experiments/v3_1/preserved_summary.csv",
        ROOT / "experiments/v3_1/generated/attachment_anger_v3_1_corrected_summary.csv",
    ),
    (
        "V5.1",
        ROOT / "experiments/v5_1/reproduce_v5_1.py",
        ROOT / "experiments/v5_1/preserved_metrics.csv",
        ROOT / "experiments/v5_1/generated/attachment_emotion_v5_1_metrics.csv",
    ),
    (
        "V6",
        ROOT / "experiments/v6/reproduce_v6.py",
        ROOT / "experiments/v6/preserved_metrics.csv",
        ROOT / "experiments/v6/generated/attachment_emotion_v6_betrayal_metrics.csv",
    ),
    (
        "V7.1",
        ROOT / "experiments/v7_1/reproduce_v7_1.py",
        ROOT / "experiments/v7_1/preserved_summary.csv",
        ROOT / "experiments/v7_1/generated/attachment_emotion_v7_1_summary.csv",
    ),
    (
        "V8.1",
        ROOT / "experiments/v8_1/reproduce_v8_1.py",
        ROOT / "experiments/v8_1/preserved_metrics.csv",
        ROOT / "experiments/v8_1/generated/attachment_emotion_v8_1_closed_loop_metrics.csv",
    ),
]


def main() -> int:
    failures: list[str] = []

    for label, script, preserved, generated in CASES:
        print(f"\n=== {label} ===")
        subprocess.run([sys.executable, str(script)], check=True, cwd=ROOT)

        expected = pd.read_csv(preserved)
        actual = pd.read_csv(generated)

        try:
            assert_frame_equal(expected, actual, check_exact=True)
        except AssertionError as exc:
            failures.append(label)
            print("FAIL: regenerated values differ from preserved values")
            print(exc)
        else:
            print(
                f"PASS: exact match ({expected.shape[0]} rows x "
                f"{expected.shape[1]} columns)"
            )

    if failures:
        print("\nValidation failed for:", ", ".join(failures))
        return 1

    print("\nALL VALIDATED EXPERIMENTS MATCH PRESERVED OUTPUTS EXACTLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
