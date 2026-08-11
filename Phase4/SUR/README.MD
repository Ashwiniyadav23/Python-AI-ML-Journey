# Supervised vs. Unsupervised vs. Reinforcement Learning — README

Reference notes on the three core machine learning paradigms, with examples and runnable code.

---

## The Core Difference — Quick Mental Model

The three types differ in **what kind of feedback the model gets while learning**.

| Type | What you give the model | What it learns |
|---|---|---|
| **Supervised** | Labeled examples (input + correct answer) | To predict the correct answer for new inputs |
| **Unsupervised** | Unlabeled data (no correct answer given) | To find hidden patterns/groupings on its own |
| **Reinforcement** | An environment + rewards/penalties | To take actions that maximize reward over time |

---

## 1. Supervised Learning — Learning With an Answer Key

**The idea:** you give the model many examples where you already know the correct answer, and it learns the pattern connecting input → output.

**Analogy:** studying with flashcards that have the answer printed on the back.

### Example — predicting exam scores

```
Hours Studied → Exam Score (already known)
1 hour   → 50
2 hours  → 55
3 hours  → 65
5 hours  → 78
8 hours  → 92
```

The model learns the pattern from these known pairs, then predicts the score for a **new** student who studied 4 hours — something it was never explicitly told.

### Example — spam detection

```
Email Text                          → Label (already known)
"Win a free iPhone now!!!"          → Spam
"Meeting moved to 3pm tomorrow"     → Not Spam
```

### The two main sub-types

- **Regression** — predicting a number (e.g. price, score)
- **Classification** — predicting a category (e.g. spam / not spam)

### Real-world examples
- Email spam filters
- House/stock price prediction
- Medical diagnosis from scans
- Credit scoring

**Key thing to remember:** every training example comes with the correct answer already attached — that's what makes it "supervised."

---

## 2. Unsupervised Learning — Finding Patterns With No Answer Key

**The idea:** you give the model data with no correct answers attached at all. It finds structure, patterns, or groupings on its own.

**Analogy:** sorting a mixed box of 100 socks with no labels — you naturally group similar-looking ones together, without anyone telling you the "correct" groups.

### Example — customer segmentation

```
Customer   Money Spent/Month   Visits/Month
Person A   $500                2
Person B   $520                3
Person C   $50                 10
Person D   $45                 12
Person E   $3000               1
```

Nobody labeled these customers as "types" — an unsupervised model notices that A & B are similar, C & D are similar, and E stands alone, grouping them accordingly.

### The two main sub-types

- **Clustering** — grouping similar items together (e.g. customer segments)
- **Dimensionality reduction** — compressing many features into fewer, meaningful ones (e.g. PCA)

### Real-world examples
- Customer segmentation for marketing
- Grouping similar news articles or products
- Anomaly/fraud detection
- Compressing features before feeding into another model

**Key thing to remember:** there's no correct answer given anywhere — the model's only job is to notice similarity or structure on its own.

---

## 3. Reinforcement Learning (RL) — Learning Through Trial and Error

**The idea:** there's no fixed dataset of correct answers. Instead, an **agent** takes **actions** in an **environment**, and receives **rewards** (good) or **penalties** (bad) based on the outcome. Over time, it learns which actions lead to the best long-term reward.

**Analogy:** training a dog to sit — you don't hand it a textbook of correct sitting positions. It tries something, and if it happens to sit, it gets a treat. Repeated over many tries, it learns which action earns the reward.

### Core building blocks

| Term | Meaning |
|---|---|
| **Agent** | The thing making decisions (the dog, the game AI, the maze-solver) |
| **Environment** | The world it operates in |
| **Action** | A choice the agent can make |
| **Reward/Penalty** | Feedback after an action |
| **Policy** | The agent's current strategy — "what action to take in each situation" |

### Real-world examples
- Game-playing AI (Chess, Go, video games)
- Robotics — learning to walk or grasp objects
- Self-driving car decision-making
- Recommendation systems that adapt to long-term engagement

### Why it's harder than the other two

In supervised learning, you're told the exact correct answer every time. In RL, the reward is often **delayed** — you only find out if an early move was good several steps later (e.g., a chess move only proves good or bad once the game ends). The agent has to figure out which of its many earlier actions actually deserves credit for a later reward.

## Side-by-Side Comparison

| | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| **Data given** | Labeled (input + correct answer) | Unlabeled (input only) | No fixed dataset — an environment to interact with |
| **Goal** | Predict the correct output for new inputs | Discover hidden structure/groups | Learn the best actions to maximize long-term reward |
| **Feedback** | Exact correct answer, every time | None — must find patterns unsupervised | Reward/penalty signal, sometimes delayed |
| **Example** | Spam filter | Customer segmentation | Game-playing AI, maze solver |
| **Analogy** | Studying with flashcards that show the answer | Sorting a messy box of socks with no instructions | Training a dog with treats for good behavior |

---

## One More Way to Remember It — Learning to Cook

- **Supervised learning** = following a recipe with exact measurements and a photo of the correct result — you know exactly what "correct" looks like, and adjust until you match it.
- **Unsupervised learning** = being handed a box of random ingredients with no recipe, and figuring out on your own which ones naturally go well together.
- **Reinforcement learning** = cooking without a recipe, tasting as you go, and adjusting based on whether it tastes good or bad — learning through repeated trial, not a fixed answer key.

---

## Quick Recap

- **Supervised** = "Here are questions AND their correct answers — learn the pattern."
- **Unsupervised** = "Here's a pile of stuff, no answers at all — find any patterns yourself."
- **Reinforcement** = "Here's a situation — try things, and I'll tell you (via reward/penalty) if that was good or bad, sometimes only after a while."