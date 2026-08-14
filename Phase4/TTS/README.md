# Train/Test/Validation Splits & Cross-Validation — README

Reference notes on why and how we split data before training a machine learning model.

---

## Why Do We Split Data At All?

**The core problem:** if you test your model on the same data it learned from, you can't tell if it actually learned a real pattern, or just memorized the answers.

**Analogy:** imagine a student who somehow got a copy of the exact exam questions AND answers beforehand, and just memorized them. They'd score 100% — but that tells you nothing about whether they actually understand the subject. Give them different questions on the same topic, and they might fail completely.

This exact problem in ML is called **overfitting** — a model that memorized the training data instead of learning the underlying pattern. Splitting data is how we catch this.

---

## 1. The Train/Test Split — The Basic Version

You divide your dataset into two separate chunks:

- **Training set** (e.g. 80%) — the model learns from this
- **Test set** (e.g. 20%) — the model NEVER sees this during training; used only at the end, to check performance on new, unseen data

```python
from sklearn.model_selection import train_test_split

# X = features (inputs), y = labels (correct answers)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(len(X_train))   # 80% of the data
print(len(X_test))    # 20% of the data
```

- `test_size=0.2` → 20% goes to testing, 80% to training
- `random_state=42` → makes the split reproducible (same split every time, instead of random each run)

### A concrete example

Say you have 1,000 house price records:
```
Training set: 800 houses → model studies these, learns the pattern
Test set: 200 houses → model has NEVER seen these before
```

After training, check: "for these 200 houses the model has never seen, how close were its price predictions to the actual prices?" That's your honest, real-world performance estimate.

> ⚠️ **Key rule:** never let the model see the test set during training. Even accidentally leaking test data into training (called **data leakage**) gives you a falsely optimistic performance number that won't hold up in the real world.

---

## 2. Why Add a Third Split — The Validation Set?

While building a model, you'll try different settings — different algorithms, different hyperparameters. If you keep checking these choices against your test set, you're indirectly "peeking" at it repeatedly, and your model selection becomes biased toward whatever happens to work well on that specific test set.

**The fix:** add a middle set, used only for tuning decisions, while the test set stays locked away until the very end.

```
Training set (e.g. 60%)   → model learns the actual patterns from this
Validation set (e.g. 20%) → used to compare different models/settings, tune hyperparameters
Test set (e.g. 20%)       → touched ONLY ONCE, at the very end, for the final honest evaluation
```

```python
from sklearn.model_selection import train_test_split

# First split: separate out the test set
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Second split: divide the remaining data into train and validation
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)
# Note: 0.25 of the remaining 80% = 20% of the original total

print(len(X_train))  # ~60%
print(len(X_val))    # ~20%
print(len(X_test))   # ~20%
```

### Analogy — studying for a big exam

- **Training set** = the textbook and practice problems you study from
- **Validation set** = practice tests you take along the way, to check "am I ready?" and decide what to study more
- **Test set** = the actual final exam — taken only once, the true measure of what you've learned

If you kept re-taking "the final exam" to decide what to study next, it would stop being a fair final exam — you'd just be memorizing that specific exam. That's why the test set is touched only once, at the very end.

---

## 3. Cross-Validation — A Smarter Way to Use Limited Data

### The problem it solves

A single train/test split has a downside: results depend somewhat on *which* rows happened to land in training vs. testing, just by chance. With a small dataset, an unlucky split could make a model look better or worse than it really is.

### The idea — K-Fold Cross-Validation

Instead of one fixed split, split the data into **K equal chunks** ("folds"), then repeat the train/test process **K times** — each time using a different chunk as the test set and the rest as training — then average the results.

**Example with K=5:**
```
Round 1: Test on Fold 1, Train on Folds 2,3,4,5
Round 2: Test on Fold 2, Train on Folds 1,3,4,5
Round 3: Test on Fold 3, Train on Folds 1,2,4,5
Round 4: Test on Fold 4, Train on Folds 1,2,3,5
Round 5: Test on Fold 5, Train on Folds 1,2,3,4
```

Every row gets used for testing **exactly once**, and for training **four times** — giving 5 separate performance scores, averaged for a much more reliable estimate.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=5)   # cv=5 means 5-fold cross-validation

print(scores)          # 5 individual scores, one per fold
print(scores.mean())   # the average — a much more reliable performance estimate
```

### Analogy — grading a class fairly

A teacher wants to know how good their teaching method is. Instead of testing it on just ONE random group of students (who might happen to be unusually strong or weak), they split the class into 5 groups, test the method on each group in turn — 5 separate mini-experiments — then average the results. Much more trustworthy than relying on a single lucky (or unlucky) group.

### Why it matters especially for small datasets

If you only have 200 data points, a single 80/20 split leaves just 40 examples for testing — not much to judge performance on, and very sensitive to which 40 got picked. Cross-validation lets **every** data point contribute to both training and testing (at different times), squeezing much more reliable signal out of a limited dataset.

---

## Putting It All Together — The Typical Real-World Workflow

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor

# Step 1: Set aside a final test set — never touched until the very end
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Use cross-validation on the remaining data to compare models/settings
model = RandomForestRegressor()
cv_scores = cross_val_score(model, X_train_val, y_train_val, cv=5)
print("Average validation score:", cv_scores.mean())

# Step 3: Once you're happy with your model choice, train on ALL the train_val data
model.fit(X_train_val, y_train_val)

# Step 4: Finally, evaluate ONCE on the untouched test set
final_score = model.score(X_test, y_test)
print("Final test score:", final_score)
```

This combines the best of both ideas: **cross-validation** for reliable model tuning, and a **held-out test set** for one final, honest check that hasn't been touched during any decision-making.

---

## Quick Summary Table

| Concept | Purpose | When it's used |
|---|---|---|
| **Training set** | The data the model actually learns from | During training |
| **Validation set** | Compare models/settings, tune hyperparameters | During model development, repeatedly |
| **Test set** | Final, honest performance check | Only once, at the very end |
| **Cross-validation** | Get a more reliable performance estimate by testing on multiple different splits | During model development, especially with smaller datasets |

---

## Why This Matters for ML

- Skipping proper splitting is the **#1 reason beginner models look great in testing but fail in the real world** — the model was accidentally evaluated (even a little) on data it had already "seen."
- Cross-validation gives confidence that a model's performance number isn't just a fluke of one lucky split.
- This exact workflow — train, validate/tune, test once — is the standard structure of every serious ML project, regardless of which algorithm is used.