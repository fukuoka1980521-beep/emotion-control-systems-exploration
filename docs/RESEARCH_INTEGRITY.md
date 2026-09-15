# Research Integrity and Interpretation Rules

## 1. What this project claims

This project investigates whether **emotion-like functional behavior** can emerge from general computational mechanisms such as value, attachment, memory, prediction error, identity-specific learning, self-models, and body-state feedback.

It does **not** claim that the simulated agents possess subjective feelings, consciousness, phenomenal experience, or human-equivalent emotion.

## 2. Functional behavior is not subjective feeling

A simulated agent may:

- protect a valued target,
- search after loss,
- alter behavior toward a repeated interferer,
- retain a negative actor model after reform,
- react strongly to expectation violation,
- defend a social self-model,
- change policy under body-state feedback.

These patterns may be functionally analogous to parts of fear, grief, anger, resentment, betrayal, humiliation, guilt, or anxiety. They are not evidence that the agent *feels* those emotions.

## 3. Negative and null findings must be retained

The project deliberately keeps results that weaken the starting hypothesis.

Examples include:

- attachment alone did not generate a jealousy-specific response in V2;
- expectation violation in V6 increased model shock but did not automatically produce the strongest punitive response;
- some apparent persistence in V5 was partly attributable to policy lock-in and insufficient sampling of new evidence;
- V7 initially produced a false-positive repair response under external loss because the action model was too permissive.

## 4. Corrections are part of the evidence

When a design error or confound is found, the original result is not silently rewritten.

Corrected versions are labeled explicitly:

- V3 → V3.1
- V5 → V5.1
- V7 → V7.1
- V8 → V8.1

This is intended to preserve the path by which the hypothesis was refined.

## 5. Human-designed structure versus learned structure

Every result must distinguish between:

### Human-designed
- reward or utility functions,
- available actions,
- environment transition rules,
- state representation,
- body-state dynamics,
- learning rules.

### Learned or interaction-derived
- actor-specific value estimates,
- policy differentiation from experience,
- persistence caused by update dynamics,
- expectation gaps,
- changes arising from closed-loop interaction.

A result is not called emergent merely because it was not represented by an emotion label.

## 6. Reproducibility standard for v1.0

The first archived release should include:

- exact code used for each retained experiment,
- fixed random seeds or documented seed procedure,
- parameters,
- raw or sufficient result tables,
- aggregate metrics,
- figures,
- correction notes,
- software/runtime information where available.

## 7. AI use disclosure

AI systems were used substantially in:

- hypothesis discussion and refinement,
- code generation,
- simulation execution,
- identification of confounds and design errors,
- interpretation,
- literature-search support,
- writing and editing.

The human originator supplied the initial conceptual question and repeatedly directed whether to continue, challenge, or extend the hypothesis. The final release should describe AI use explicitly rather than implying that the work was conducted without AI assistance.

## 8. External communication rule

Preferred wording:

> The simulations produced functional patterns analogous to selected components of emotion.

Avoid wording such as:

> The AI felt fear.

> We created genuine emotion.

> This proves how human emotion works.

The simulations are hypothesis-generating computational experiments, not direct evidence about conscious experience.
