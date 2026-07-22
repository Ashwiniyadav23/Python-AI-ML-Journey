# Python Control Flow —

Reference notes on **if-else**, **for loop**, **while loop**, and **do-while (simulated)** in Python.

---

## 1. if / else — Decision Making

Checks a condition and runs different code depending on whether it's True or False.

```python
num = 5

if num % 2 == 0:
    print("even number")
else:
    print("odd number")
```
Output:
```
odd number
```

> ⚠️ **Note:** in the original snippet the condition used `n % 2 == 0` while the variable was defined as `num = 5`. Since `n` was never defined, this would raise a `NameError: name 'n' is not defined`. Always make sure the variable name in the condition matches the one you declared — fixed above by using `num` consistently.

**How it works:**
- `num % 2` gives the remainder when `num` is divided by 2
- If remainder is `0` → the number is even
- Otherwise → it's odd

---

## 2. for Loop — Repeat a Fixed Number of Times

```python
num = 10
sum = 0

for i in range(num):
    sum += i

print(sum)
```
Output:
```
45
```

**How it works:**
- `range(num)` generates numbers `0, 1, 2, ... 9` (10 numbers, stopping before `num`)
- Each loop, `i` takes the next number, and `sum += i` adds it to the running total
- `sum += i` is shorthand for `sum = sum + i`

**Manually tracing it:**
```
i=0 → sum=0
i=1 → sum=1
i=2 → sum=3
i=3 → sum=6
...
i=9 → sum=45
```

---

## 3. while Loop — Repeat Until a Condition Becomes False

```python
s = 3
i = 1
sum = 0

while i <= s:
    sum += i
    i = i + 1

print(sum)
```
Output:
```
6
```

**How it works:**
- The condition `i <= s` is checked **before** each run
- Loop runs while `i` is 1, 2, 3 (all `<= 3`), adding each to `sum`
- `i = i + 1` increases `i` each time — without this, the loop would run forever (an **infinite loop**)

**Manually tracing it:**
```
i=1 → sum=1 → i becomes 2
i=2 → sum=3 → i becomes 3
i=3 → sum=6 → i becomes 4
i=4 → condition (4 <= 3) is False → loop stops
```

---

## 4. do-while Loop (Simulated) — Run at Least Once, Then Check

Python has no built-in `do-while` keyword. It's simulated using `while True:` with a `break` at the end, so the code always runs **at least once** before the condition is checked.

```python
count = 0

while True:
    print("Count:", count)   # runs first
    count += 1

    if count >= 3:           # condition checked after
        break
```
Output:
```
Count: 0
Count: 1
Count: 2
```

**How it works:**
- `while True:` means "keep looping forever" — unless something inside stops it
- The `print` and `count += 1` always run at least once, no matter what
- The `if count >= 3: break` is checked **after** the code runs — once true, it exits the loop

---

## Quick Comparison Table

| Loop Type | Condition Checked | Runs at Least Once? | Best Used When |
|---|---|---|---|
| `for` | N/A — loops over a fixed sequence | Yes, if the sequence isn't empty | You know how many times to repeat (a list, a range) |
| `while` | Before running the code | No — skips entirely if condition starts False | You don't know in advance how many times — depends on a changing condition |
| `do-while` (simulated) | After running the code | Yes — always | You need the code to run at least once regardless (e.g., asking for input) |

---

## Why This Matters for ML

- **`if/else`** is how you'll filter data and set thresholds — e.g., "if predicted probability > 0.5, classify as spam."
- **`for` loops** are how you'll iterate through rows of a dataset, or through epochs (training rounds) when training a model.
- **`while` loops** are used in training loops that keep running until a model's error is small enough, or until a set condition is met.
- **`do-while` style loops** are useful for input validation — like re-prompting a user (or re-checking a data source) until you get a valid result.