
# 📌 SECTION 2: Operators

## What is an Operator?

An operator performs an action on values — calculating, comparing, or combining them.

---

## A) Arithmetic Operators — Calculate

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponent (power) | `10 ** 2` | `100` |

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

**Real example — splitting a bill:**
```python
total_bill = 100
people = 3

print(total_bill // people)   # 33  → each person pays
print(total_bill % people)    # 1   → amount left over
```

---

## B) Comparison Operators — Compare

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal | `10 >= 10` | `True` |
| `<=` | Less than or equal | `10 <= 5` | `False` |

```python
x = 10
y = 20

print(x > y)    # False
print(x < y)    # True
print(x == y)   # False
print(x != y)   # True
```

⚠️ **Common mistake:** `=` assigns a value, `==` checks equality. Mixing these up is one of the most common beginner errors.

**Real example — checking voting eligibility:**
```python
age = 19
print(age >= 18)   # True → eligible to vote
```

---

## C) Logical Operators — Combine

| Operator | Meaning | Example |
|---|---|---|
| `and` | True only if BOTH sides are True | `True and False` → `False` |
| `or` | True if AT LEAST ONE side is True | `True or False` → `True` |
| `not` | Flips True ↔ False | `not True` → `False` |

```python
age = 25
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)   # True

is_raining = False
print(not is_raining)   # True
```

**Real example — loan eligibility check:**
```python
income = 50000
credit_score = 720
has_debt = False

qualifies = (income > 30000) and (credit_score >= 700) and (not has_debt)
print(qualifies)   # True
```

---

## Quick Reference Table — All Operators

| Category | Operators |
|---|---|
| Arithmetic | `+`  `-`  `*`  `/`  `//`  `%`  `**` |
| Comparison | `==`  `!=`  `>`  `<`  `>=`  `<=` |
| Logical | `and`  `or`  `not` |

---

## Why Operators Matter in ML

- **Arithmetic operators** are the building blocks of every formula a model uses to make predictions.
- **Comparison operators** are how you filter and clean data (e.g., "keep only rows where age >= 18").
- **Logical operators** let you combine multiple conditions at once — critical for filtering real-world, messy datasets.

```python
# Example: filtering a dataset using comparison + logical operators together
filtered_data = data[(data["age"] >= 18) & (data["income"] > 30000)]
```