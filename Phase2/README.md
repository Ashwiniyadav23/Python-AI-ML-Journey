# Linear Algebra in Python (From Scratch) — README

Reference notes covering **scalars, vectors, matrices**, and **matrix multiplication implemented by hand** (no NumPy) — based on `start.py`, `matrix.py`, `vector.py`, and `matrix_multiplication.py`.

---

## 1. `start.py` — Scalars, Vectors, and Matrices

```python
# A single value (Scalar)
num = 12

# A list of values (Vector)
vector = [1, 2, 3, 4]

# A table of values stored in rows and columns (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

**What each one is:**

| Term | What it is | Example |
|---|---|---|
| **Scalar** | A single number | `num = 12` |
| **Vector** | An ordered list of numbers | `vector = [1, 2, 3, 4]` |
| **Matrix** | A grid of numbers — rows and columns | `matrix = [[1,2,3],[4,5,6]]` |

A matrix is really just a **list of lists** — each inner list is one row.

```python
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]
```

> **Key idea:** Matrix multiplication combines information from two matrices — it is **NOT** just placing two matrices side by side or merging their values directly. The rules for *how* they combine are covered below.

---

## 2. `matrix.py` — Counting Rows/Columns, and Two Different Loop Patterns

### Counting rows and columns

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])

print("Rows:", rows)       # Rows: 2
print("Columns:", columns) # Columns: 3
```

**How it works:**
- `len(matrix)` → counts how many rows (how many inner lists) → `2`
- `len(matrix[0])` → looks at the **first row** and counts how many items are in it → `3`

### Summing every value in a matrix (commented out in your file)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum = sum + matrix[i][j]

print(sum)   # 21
```

**How it works:** the outer loop (`i`) walks through each row, the inner loop (`j`) walks through each value in that row, and every value gets added to `sum`.

### ⚠️ About the code labeled "matrix multiplication" in `matrix.py`

```python
matrix_multiplication = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

sum = 1
for i in range(len(matrix_multiplication)):
    for j in range(len(matrix_multiplication[i])):
        sum = sum * matrix_multiplication[i][j]

print(sum)   # 40320
```

This code actually calculates the **product of every number inside one single matrix** (`1×2×3×4×5×6×7×8 = 40320`) — it multiplies all values in one matrix together into a single number.

This is **different from real matrix multiplication**, which combines **two separate matrices** together to produce a new matrix (not a single number). Real matrix multiplication is shown correctly in `vector.py` and `matrix_multiplication.py`, explained next.

---

## 3. `vector.py` / `matrix_multiplication.py` — Real Matrix Multiplication (By Hand)

```python
A = [
    [2, 3],
    [4, 5]
]

B = [
    [10],
    [20]
]

result = [
    [0],
    [0]
]  # for storing result

for i in range(len(A)):          # Rows of A
    for j in range(len(B[0])):   # Columns of B
        for k in range(len(B)):  # Common dimension
            result[i][j] += A[i][k] * B[k][j]

print(result)   # [[80], [130]]
```

### Breaking down what's happening, step by step

We're multiplying matrix `A` (2×2) by matrix `B` (2×1). The result will be a 2×1 matrix.

**The three loops mean:**
- `i` → walks through each **row of A**
- `j` → walks through each **column of B**
- `k` → walks through the **shared/common dimension** (columns of A = rows of B), used to do the actual multiplying-and-adding

**Manually tracing `result[0][0]`** (row 0 of A, column 0 of B):
```
result[0][0] = A[0][0]×B[0][0] + A[0][1]×B[1][0]
             = 2×10 + 3×20
             = 20 + 60
             = 80
```

**Manually tracing `result[1][0]`** (row 1 of A, column 0 of B):
```
result[1][0] = A[1][0]×B[0][0] + A[1][1]×B[1][0]
             = 4×10 + 5×20
             = 40 + 100
             = 140
```

Running this code confirms the output:
```
[[80], [140]]
```
This matches the manual trace exactly — the loop logic is correct.

### Why 3 nested loops?

This is the **general recipe for matrix multiplication**, and it works for matrices of any size (not just 2×2 by 2×1):
1. For every row in A...
2. ...and every column in B...
3. ...multiply matching elements and add them up (this inner step is a **dot product**)

This is exactly the same dot-product idea from earlier — matrix multiplication is just "many dot products, one for each row/column pairing."

---

## Quick Summary Table

| File | What it demonstrates |
|---|---|
| `start.py` | Defining a scalar, vector, and matrix |
| `matrix.py` | Counting rows/columns; summing all values; (mislabeled) product of all values |
| `vector.py` / `matrix_multiplication.py` | Real matrix multiplication using 3 nested loops (by hand, no NumPy) |

---

## The NumPy Version (For Comparison)

Everything above works, but real projects use NumPy instead of writing nested loops by hand — it's faster and far less code:

```python
import numpy as np

A = np.array([[2, 3], [4, 5]])
B = np.array([[10], [20]])

result = A @ B     # or: np.matmul(A, B)
print(result)
```

**Why learn the by-hand version first?** Writing the triple-loop version yourself is exactly how you build real intuition for *what* matrix multiplication is doing — once that clicks, `A @ B` in NumPy stops looking like a black box and just looks like a fast shortcut for the same thing.

---

## Why This Matters for ML

- Every neural network layer computes `output = input @ weights + bias` — that `@` is precisely the triple-loop operation you wrote by hand above, just done instantly on much larger matrices.
- Understanding the row/column-matching rule (columns of A must match rows of B) is *the* most common source of shape-mismatch errors when building models — knowing the mechanics helps you debug those errors instead of guessing.