# NumPy — README

Reference notes on **NumPy**, Python's core library for fast numerical computing.

---

## What is NumPy?

> **"NumPy is a Python library for fast numerical computing using arrays."**

---

## Why NumPy?

Suppose you have marks:
```
80
90
70
60
```

You want to add 5 bonus marks to each one.

### Using a plain Python list — you need a loop

```python
marks = [80, 90, 70, 60]

new_marks = []

for i in marks:
    new_marks.append(i + 5)

print(new_marks)
```

Output:
```
[85, 95, 75, 65]
```

This works, but you had to manually write a loop, create an empty list, and append to it one value at a time.

### Using NumPy — no loop needed

```python
import numpy as np

marks = np.array([12, 34, 5, 6])
print(marks + 5)
```

Output:
```
[17 39 10 11]
```

**One line — `marks + 5` — added 5 to every single value at once.** No loop, no empty list, no `.append()`. This is the core idea behind NumPy: operations apply to the **whole array simultaneously**, instead of one item at a time.

This is called **vectorization**, and it's the main reason NumPy exists — it's both shorter to write *and* dramatically faster to run, especially as the amount of data grows into thousands or millions of values.

---

## Why NumPy Is Faster Than Plain Python Lists

Plain Python lists check and process each item one at a time, with extra overhead per item. NumPy arrays store all values as the **same data type**, packed tightly in memory, and run the actual math using pre-compiled, optimized code underneath — Python just gives you a simple interface on top.

```python
import time
import numpy as np

numbers = list(range(1000000))

# Plain Python list
start = time.time()
squared = [x**2 for x in numbers]
print("List time:", time.time() - start)

# NumPy array
arr = np.array(numbers)
start = time.time()
squared_np = arr ** 2
print("NumPy time:", time.time() - start)
```

NumPy is typically **10–100x faster** for this kind of operation.

---

## Creating Arrays

```python
import numpy as np

# From a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)   # [1 2 3 4 5]

# 2D array (like a matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# [[1 2 3]
#  [4 5 6]]

# Common shortcuts
zeros = np.zeros((3, 3))         # a 3x3 grid of zeros
ones = np.ones((2, 4))            # a 2x4 grid of ones
range_arr = np.arange(0, 10, 2)   # [0 2 4 6 8]  — like Python's range()
random_arr = np.random.rand(3)    # 3 random numbers between 0 and 1
```

---

## Checking Shape and Size

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix.shape)   # (2, 3) → 2 rows, 3 columns
print(matrix.ndim)    # 2 → number of dimensions
print(matrix.size)    # 6 → total number of elements
```

**Why this matters:** almost every ML bug involving a "shape mismatch" comes down to not tracking `.shape` carefully — checking shapes constantly is a core habit.

---

## Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])        # 10  → first element
print(arr[-1])       # 50  → last element
print(arr[1:4])      # [20 30 40]  → slice

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[0, 2])   # 3  → row 0, column 2
print(matrix[:, 1])   # [2 5]  → ALL rows, column 1 only
print(matrix[1, :])   # [4 5 6]  → row 1, ALL columns
```

The `:` means "give me everything along this dimension" — useful for pulling out a whole column or row at once.

---

## Vectorized Operations

Instead of looping through each item, an operation is applied to the **entire array at once** — this is exactly the `marks + 5` example from above, generalized:

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)     # [11 12 13 14 15]  → adds 10 to every element
print(arr * 2)      # [2 4 6 8 10]      → multiplies every element by 2
print(arr ** 2)      # [1 4 9 16 25]     → squares every element
```

---

## Broadcasting — Combining Arrays of Different Sizes

NumPy automatically "stretches" smaller arrays to match bigger ones when doing math.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
add_vector = np.array([10, 20, 30])

result = arr + add_vector
print(result)
# [[11 22 33]
#  [14 25 36]]
```

Here, `add_vector` (just 3 numbers) got automatically applied to **every row** of the 2×3 matrix — no manual repeating needed.

---

## Useful Aggregate Functions

```python
scores = np.array([85, 90, 78, 92, 60])

print(scores.sum())      # 405   → total
print(scores.mean())     # 81.0  → average
print(scores.max())      # 92
print(scores.min())      # 60
print(scores.std())      # standard deviation
print(np.sort(scores))   # [60 78 85 90 92]
```

---

## Filtering with Conditions (Boolean Indexing)

```python
scores = np.array([85, 90, 78, 92, 60])

passing = scores[scores >= 80]
print(passing)   # [85 90 92]
```

`scores >= 80` first creates `[True, True, False, True, False]`, and then `scores[...]` keeps only the values where that condition is `True`. This exact pattern is everywhere in data cleaning, e.g. `data[data["age"] >= 18]`.

---

## Reshaping Arrays

```python
arr = np.arange(12)           # [0 1 2 3 4 5 6 7 8 9 10 11]
reshaped = arr.reshape(3, 4)   # reorganize into 3 rows, 4 columns

print(reshaped)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

**Why this matters:** images are often flattened into a long list of pixel values, then reshaped back into a 2D grid (height × width) for processing — reshaping is a constant operation in computer vision work.

---

## Matrix Multiplication

```python
A = np.array([[2, 3], [4, 5]])
B = np.array([[10], [20]])

result = A @ B          # or np.matmul(A, B)
print(result)
# [[ 80]
#  [140]]
```

This is the same result as writing your own triple-nested loop by hand — NumPy just does it instantly, using one symbol (`@`).

---

## Quick Summary Table

| Feature | Example | Purpose |
|---|---|---|
| Creating arrays | `np.array([1,2,3])` | Store numbers efficiently |
| Shape checking | `.shape`, `.ndim`, `.size` | Understand your data's structure |
| Indexing/slicing | `arr[1:4]`, `matrix[:, 1]` | Access specific parts of the data |
| Vectorized math | `arr * 2`, `arr + 10` | Apply operations to everything at once, fast |
| Broadcasting | `matrix + vector` | Combine differently-shaped arrays automatically |
| Aggregates | `.sum()`, `.mean()`, `.std()` | Summarize data quickly |
| Boolean filtering | `arr[arr >= 80]` | Keep only values meeting a condition |
| Reshaping | `.reshape(3, 4)` | Reorganize data's dimensions |
| Matrix multiplication | `A @ B` | Core operation behind ML models |

---

## Why NumPy Matters for ML

- **Every ML library is built on it** — Pandas DataFrames store data as NumPy arrays underneath; PyTorch/TensorFlow tensors work almost identically to NumPy arrays, just with GPU support added.
- **Speed matters at scale** — datasets with millions of rows would be painfully slow with plain Python loops; NumPy's vectorized operations make large-scale ML computation feasible.
- **The mental model transfers directly** — once you're comfortable with NumPy's shape/indexing/broadcasting rules, PyTorch and TensorFlow tensors feel almost identical to learn, since they deliberately copied NumPy's design.