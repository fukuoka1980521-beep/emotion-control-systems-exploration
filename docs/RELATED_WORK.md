# Related Work

This document positions the exploratory V1–V8.1 simulation series against established research. The project does **not** claim that computational emotion modeling is new. Its potential contribution is the transparent sequence by which a simple attachment-centered hypothesis was repeatedly tested, falsified in part, and expanded only when simpler mechanisms failed.

## 1. Reinforcement learning and computational emotion

Moerland, Broekens, and Jonker surveyed computational emotion models in reinforcement-learning agents and robots. Their review shows that emotion-like variables can be derived from value, appraisal, homeostasis, and other decision-system quantities, and that RL agents can serve as testbeds for emotion theories.

**Reference**  
Moerland, T. M., Broekens, J., & Jonker, C. M. (2018). *Emotion in reinforcement learning agents and robots: a survey*. Machine Learning, 107, 443–480. https://doi.org/10.1007/s10994-017-5666-0

**Relation to this project**  
V1–V4 are closest to this tradition. The present project should therefore not claim novelty for deriving emotion-like signals from value-learning systems. Its narrower question is how far a deliberately minimal attachment-centered model can be pushed before additional representational structure becomes necessary.

## 2. Appraisal signals emerging from learning systems

Sequeira, Melo, and Paiva investigated whether useful appraisal-like signals can arise from reinforcement-learning mechanisms rather than being manually encoded as emotion categories.

**Reference**  
Sequeira, P., Melo, F. S., & Paiva, A. (2015). *Emergence of emotional appraisal signals in reinforcement learning agents*. Autonomous Agents and Multi-Agent Systems, 29, 537–568. https://doi.org/10.1007/s10458-014-9262-4

**Relation to this project**  
This is particularly relevant to the principle used throughout V1–V8.1: avoid variables named fear, grief, jealousy, guilt, and so forth, and examine whether generic computational variables can generate functionally similar patterns.

## 3. Limits and ad-hoc structure in computational emotion models

Ojha, Vitale, and Williams reviewed computational emotion models and highlighted persistent limitations, including difficulty generalizing across situations and the tendency for implementations to rely on ad-hoc mappings between appraisal variables and emotion intensity.

**Reference**  
Ojha, S., Vitale, J., & Williams, M.-A. (2021). *Computational emotion models: a thematic review*. International Journal of Social Robotics, 13, 1253–1279. https://doi.org/10.1007/s12369-020-00713-1

**Relation to this project**  
The corrective sequence V3→V3.1, V5→V5.1, and V7→V7.1 is important because it exposes exactly this risk: apparent emotion-like behavior can be produced by permissive utility functions or action effects. The corrections are therefore part of the evidence, not merely implementation cleanup.

## 4. Homeostatic reinforcement learning

Keramati and Gutkin developed a formal reinforcement-learning framework in which reward value is tied to physiological need reduction and internal-state stability.

**Reference**  
Keramati, M., & Gutkin, B. (2014). *Homeostatic reinforcement learning for integrating reward collection and physiological stability*. eLife, 3, e04811. https://doi.org/10.7554/eLife.04811

**Relation to this project**  
V8 and V8.1 overlap with this broad idea that internal physiological state can alter valuation and behavior. The present simulations are much simpler and should not be presented as a competing homeostatic theory.

## 5. Interoception, prediction, and emotion

Seth proposed an interoceptive-inference account in which emotion and embodied selfhood are linked to predictive models of bodily signals. Seth and Friston later developed the active-interoceptive-inference perspective further.

**References**  
Seth, A. K. (2013). *Interoceptive inference, emotion, and the embodied self*. Trends in Cognitive Sciences, 17(11), 565–573. https://doi.org/10.1016/j.tics.2013.09.007

Seth, A. K., & Friston, K. J. (2016). *Active interoceptive inference and the emotional brain*. Philosophical Transactions of the Royal Society B, 371, 20160007. https://doi.org/10.1098/rstb.2016.0007

**Relation to this project**  
V8.1 is most relevant: body state becomes both an outcome of action and an input to later action selection. The simulation does not implement predictive coding or active inference, but it supports the narrower methodological point that body-state feedback should be modeled as a loop rather than a static input.

## 6. Self-conscious emotions and self-models

Research on shame, guilt, pride, embarrassment, and related self-conscious emotions emphasizes self-evaluation, social valuation, moral standards, and representations of the self in relation to others.

**References**  
Leary, M. R. (2007). *Motivational and Emotional Aspects of the Self*. Annual Review of Psychology, 58, 317–344. https://doi.org/10.1146/annurev.psych.58.110405.085658

Sznycer, D. (2019). *Forms and Functions of the Self-Conscious Emotions*. Trends in Cognitive Sciences, 23(2), 143–157. https://doi.org/10.1016/j.tics.2018.11.007

Tangney, J. P., Stuewig, J., & Mashek, D. J. (2007). *Moral emotions and moral behavior*. Annual Review of Psychology, 58, 345–372. https://doi.org/10.1146/annurev.psych.56.091103.070145

**Relation to this project**  
V7.1's competence, social-regard, and integrity dimensions are consistent with the broad idea that self-conscious emotions depend on self-representation and social or moral evaluation. They are not a validated psychological decomposition of shame, humiliation, or guilt.

## 7. Expectation discrepancy and self-discrepancy

Prior psychological work has linked discrepancies between actual and ideal self-states to shame, guilt, and pride, while predictive and reinforcement-learning frameworks emphasize prediction errors as learning signals.

**Example reference**  
Castonguay, A. L., Brunet, J., Ferguson, L., & Sabiston, C. M. (2012). *Weight-related actual and ideal self-states, discrepancies, and shame, guilt, and pride*. Body Image, 9(4), 488–494. https://doi.org/10.1016/j.bodyim.2012.07.003

**Relation to this project**  
V6 distinguishes two quantities that should not be collapsed: prediction-error magnitude ('shock') and the learned expectation that an actor will cause future harm ('control/punishment policy'). This separation is one of the clearer findings of the exploratory series.

## 8. What may be distinctive about this project

No strong priority claim is made. The potentially useful aspect is the **experimental trajectory**:

1. begin with attachment as a minimal candidate,
2. test several contexts,
3. retain failures such as the absence of jealousy,
4. add only the missing representational component suggested by the failure,
5. perform ablations and corrective reruns when confounds are found,
6. end with a layered control-system account rather than a single emotion variable.

The current working interpretation is therefore not 'attachment causes all emotion.' Instead:

> Attachment/value appears to provide one weighting mechanism, while the form of an emotion-like response depends on representations of events, actors, self, predictions, learning dynamics, information sampling, and bodily state.

## 9. Publication boundary

The external report should describe this as an **exploratory computational study / hypothesis-generating simulation series**. It should not be described as:

- a validated new theory of human emotion,
- evidence that AI is conscious,
- evidence that simulated agents literally feel emotion,
- the first computational emotion model.

A stronger scientific claim would require preregistered predictions and independent human or animal data capable of falsifying the model.
