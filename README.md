# Emotion Control Systems Exploration

Exploratory computational experiments on attachment, memory, prediction error, self-models, and body-state feedback in emotion-like agent behavior.

## Status

**Pre-release research repository.** The experiments are complete through V8.1, but the public research package is still being prepared. A DOI release has **not** yet been issued.

## Core question

Can emotion-like functional patterns emerge in artificial agents from general control mechanisms such as value, attachment, memory, prediction, self-models, and body-state feedback, without directly programming named emotions such as fear, grief, anger, jealousy, shame, or guilt?

The project began from a deliberately simple hypothesis:

> Attachment may be a major gateway into emotion-like behavior.

The experiments were then designed to break, narrow, or refine that hypothesis rather than to confirm it.

## Current working model

The experiments do **not** support the claim that attachment alone explains emotion. A better working model is:

> emotion-like functional response ≈ value / attachment × world model × memory × prediction error × self-model × body state

with persistence further affected by learning rate and by which new evidence the agent chooses to sample.

This is a model of **functional emotion-like behavior**, not evidence of subjective feeling or consciousness in AI.

## Experiment series

| Version | Main question | Key result |
|---|---|---|
| V1 | Can attachment produce simple emotion-like behavior? | Protection, search after loss, and reunion-related value changes emerged functionally. |
| V2 | Can one attachment variable generate several distinct patterns? | Threat, loss, recovery, and obstruction differentiated; jealousy did not emerge from attachment alone. |
| V3 / V3.1 | What separates obstruction handling from anger-like actor-directed response? | Cause, intentionality, and unjustified interference changed actor-directed behavior; a design leak was corrected in V3.1. |
| V4 | Can actor-directed intervention be learned without explicit fairness or anger rules? | Identity-specific memory plus outcome learning differentiated persistent, accidental, and protective actors. |
| V5 / V5.1 | Can resentment-like persistence arise after an actor reforms? | Persistence depended on memory update and on whether the agent sampled new evidence; policy lock-in was identified as a confound. |
| V6 | Does betrayal depend on expectation gap? | Equal harm produced very different prediction errors depending on prior expectations; shock and punishment separated. |
| V7 / V7.1 | Can self-model threat produce shame-, humiliation-, or guilt-like functional patterns? | Competence, social regard, and integrity losses produced different repair policies; a false-positive design error was corrected in V7.1. |
| V8 / V8.1 | Does body state modulate and feed back into emotion-like control? | Arousal, fatigue, pain, memory, action, and damage formed a closed-loop control system that altered later defensive responses. |

## Research integrity rules

This repository follows several rules that are important to interpreting the results:

- Null and inconvenient results are retained.
- Failed or flawed experimental designs are documented rather than hidden.
- Corrected versions are labeled separately instead of silently replacing earlier conclusions.
- A functional behavior pattern is never treated as proof of subjective emotion.
- Human-designed reward functions and action effects are explicitly separated from patterns that emerged through learning or interaction.
- Claims are limited to what the simulations support.

See `docs/RESEARCH_INTEGRITY.md` for details.

## Relation to prior work

This project is **not** presented as the first computational model of emotion. It overlaps with established research in computational emotion, reinforcement learning, appraisal theory, homeostatic regulation, interoceptive inference, and self-conscious emotion.

A focused literature comparison is maintained in `docs/RELATED_WORK.md`.

Key starting points include:

- Moerland, Broekens & Jonker (2018), *Emotion in reinforcement learning agents and robots: a survey*. https://doi.org/10.1007/s10994-017-5666-0
- Sequeira, Melo & Paiva (2015), *Emergence of emotional appraisal signals in reinforcement learning agents*. https://doi.org/10.1007/s10458-014-9262-4
- Ojha, Vitale & Williams (2021), *Computational emotion models: a thematic review*. https://doi.org/10.1007/s12369-020-00713-1
- Keramati & Gutkin (2014), *Homeostatic reinforcement learning for integrating reward collection and physiological stability*. https://doi.org/10.7554/eLife.04811
- Seth (2013), *Interoceptive inference, emotion, and the embodied self*. https://doi.org/10.1016/j.tics.2013.09.007
- Seth & Friston (2016), *Active interoceptive inference and the emotional brain*. https://doi.org/10.1098/rstb.2016.0007
- Sznycer (2019), *Forms and Functions of the Self-Conscious Emotions*. https://doi.org/10.1016/j.tics.2018.11.007

## Repository roadmap before v1.0

Before the first DOI release, this repository will receive:

1. experiment code and reproducible parameters,
2. summary and raw result tables,
3. figures,
4. the integrated research report,
5. AI-use disclosure,
6. citation metadata,
7. license information,
8. a frozen v1.0 release for archival deposit.

## AI-use disclosure

AI systems were used substantially in the exploratory process, including discussion, model implementation, simulation execution, error discovery, revision, literature search support, and drafting. The research package will explicitly document that role rather than presenting the work as unaided human analysis.

## License

License terms will be finalized before the v1.0 DOI release. Until then, no reuse license should be inferred from the public visibility of this repository.
