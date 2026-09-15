# Reproducibility Status

## Why this file exists

This research series was developed interactively with AI assistance. Some experiments were executed from preserved standalone scripts; others were executed in an interactive notebook/tool environment before the publication repository existed.

For research integrity, the repository must not claim stronger reproducibility than is currently demonstrated.

## Current status

### Preserved exact source

- V1: standalone Python script preserved.

### Outputs preserved

The result tables, reports, and figures generated during V1–V8.1 have been preserved locally and are being migrated into this repository.

### Source reconstruction required before v1.0 DOI release

For V2–V8.1, the experiment logic and executed code are preserved in the AI-assisted development record, but not every version currently exists as a standalone, independently rerunnable `.py` file in this repository.

Before the DOI-bearing v1.0 release, each published experiment must be assigned one of these evidence labels:

- `EXACT_REPRODUCIBLE`: preserved source reruns and reproduces the published metrics within expected stochastic tolerance.
- `RECONSTRUCTED_AND_VALIDATED`: source reconstructed from the executed record, then rerun and compared against the preserved outputs.
- `OUTPUT_ONLY`: preserved result output exists, but exact source has not yet been independently validated.

No `OUTPUT_ONLY` experiment should be presented as fully reproducible.

## Required validation procedure

For each experiment:

1. save the exact or reconstructed code in `experiments/`;
2. pin the relevant Python/package environment where practical;
3. record random seed(s), number of runs, and parameters;
4. rerun the script;
5. compare regenerated metrics with the preserved published values;
6. explain any mismatch rather than silently replacing the historical result;
7. retain corrected versions separately where a design flaw was found.

## Known corrective experiments

The series intentionally retains design failures and corrections, including:

- V3 → V3.1: removal of impossible actor-directed actions from the natural-obstruction condition;
- V5 → V5.1: separation of memory persistence from policy-lock / insufficient exploration effects;
- V7 → V7.1: removal of a false-positive mechanism that rewarded self-repair actions even when the corresponding self-model dimension had not been damaged.

These corrections are part of the evidence history and must remain visible in the final report.

## Publication rule

The final external report may describe the entire exploratory sequence, but the repository must identify the reproducibility status of every quantitative result.
