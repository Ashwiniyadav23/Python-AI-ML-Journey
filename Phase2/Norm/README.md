# Norm (Vector Length) — 

Reference notes on the **norm** of a vector — how to measure how "long" a vector is — implemented by hand with `math.sqrt`.

---

## What is a Norm?

The **norm** tells you the length (magnitude) of a vector — a single number describing how "big" the vector is, regardless of its direction.

```python
import math

A = [3, 4]

norm = math.sqrt(A[0]**2 + A[1]**2)

print(norm)

# Output:
# 5.0
```

---

## Step-by-Step Breakdown

**The vector:**
```
A = [3, 4]
```

**The formula (this is the Pythagorean theorem):**
```
norm = √(A[0]² + A[1]²)
     = √(3² + 4²)
     = √(9 + 16)
     = √25
     = 5.0
```

**How the code does this:**
- `A[0]**2` → squares the first value: `3**2 = 9`
- `A[1]**2` → squares the second value: `4**2 = 16`
- `math.sqrt(...)` → takes the square root of the sum: `√25 = 5.0`

---

## Why "Pythagorean Theorem"?

If you draw `A = [3, 4]` as an arrow on a graph — starting at `(0,0)` and ending at the point `(3, 4)` — you can picture a right-angled triangle:
- One side has length `3` (horizontal distance)
- Another side has length `4` (vertical distance)
- The norm is the length of the **diagonal** connecting the start to the end — exactly what the Pythagorean theorem (`a² + b² = c²`) calculates.

This is why the norm is also called the vector's **magnitude** — it's literally the straight-line distance from the origin to the point the vector represents.

---

## Extending to Vectors With More Than 2 Values

The same idea scales to any number of dimensions — just keep squaring each value, adding them all up, then take the square root:

```python
import math

A = [3, 4, 12]

norm = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
print(norm)   # 13.0
```

A more general version using a loop, so it works for a vector of *any* length:

```python
import math

A = [3, 4, 12]

sum_of_squares = 0
for value in A:
    sum_of_squares += value ** 2

norm = math.sqrt(sum_of_squares)
print(norm)   # 13.0
```

---

## The NumPy Version (For Comparison)

```python
import numpy as np

A = np.array([3, 4])
norm = np.linalg.norm(A)

print(norm)   # 5.0
```

Same result, no manual squaring/summing/square-rooting needed — `np.linalg.norm()` handles it directly, and works for vectors of any length automatically.

---

## Why This Matters for ML

- **Measuring distance between two points/data examples:** subtracting two vectors and taking the norm of the result tells you how "far apart" they are — used in algorithms like K-Nearest Neighbors, and in measuring similarity between data points.
- **Regularization:** many ML models penalize large weight values to avoid overfitting — this penalty is often calculated using the norm of the model's weight vector, discouraging any single weight from becoming extreme.
- **Normalizing vectors:** dividing a vector by its own norm rescales it to have a length of exactly 1, while keeping its direction the same — a common preprocessing step before feeding data into a model.