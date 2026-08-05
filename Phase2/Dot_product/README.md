# Dot Product (From Scratch) — README

Reference notes on the **dot product**, implemented by hand with a plain Python loop.

---

## What is the Dot Product?

The dot product is calculated by multiplying **corresponding elements** of two vectors and **adding the results** together.

```python
A = [1, 2, 3]
B = [4, 5, 6]

dot = 0

for i in range(len(A)):
    dot += A[i] * B[i]

print("Dot Product =", dot)

# Output:
# Dot Product = 32
```

---

## Step-by-Step Breakdown

**The vectors:**
```
A = [1, 2, 3]
B = [4, 5, 6]
```

**The rule:** multiply matching positions together, then add all the products up.

```
A[0]×B[0] = 1×4 = 4
A[1]×B[1] = 2×5 = 10
A[2]×B[2] = 3×6 = 18

Total = 4 + 10 + 18 = 32
```

**How the loop does this:**
- `dot = 0` → start the running total at zero
- `for i in range(len(A))` → walk through each index (`0, 1, 2`) since both vectors are the same length
- `dot += A[i] * B[i]` → multiply the matching pair, and add it to the running total
- After the loop finishes, `dot` holds the final sum: `32`

---

## Requirement: Vectors Must Be the Same Length

The dot product only makes sense when both vectors have the same number of elements — `range(len(A))` assumes `B` has at least as many items as `A`. If the vectors were different lengths, this code would either throw an `IndexError` or silently give a wrong/incomplete result, depending on which vector is shorter.

---

## The NumPy Version (For Comparison)

```python
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.dot(A, B))   # 32
```

Same result, no loop needed — NumPy's `np.dot()` handles the multiply-and-add pattern internally, and does it far faster for large vectors.

---

## Why This Matters for ML

- The dot product is the **building block of matrix multiplication** — every entry in a matrix multiplication result is really just one dot product between a row and a column.
- It's also how a single neuron/prediction is calculated in ML: multiplying inputs by their weights and summing them up — `prediction = (input1×weight1) + (input2×weight2) + ...` is a dot product.
- It's used to measure **similarity** between two vectors (e.g., comparing two pieces of text turned into number vectors) — a higher dot product generally means the vectors point in a more similar direction.