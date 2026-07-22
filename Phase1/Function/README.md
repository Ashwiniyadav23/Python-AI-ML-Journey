# Python Functions 

Reference notes on the different **types of functions** in Python, with examples.

---

## 1. Built-in Functions

Functions that come ready-made with Python — no need to define them yourself.

```python
print("Hello")        # built-in function to display output
len([1, 2, 3])         # built-in function to get length → 3
type(10)               # built-in function to check type → <class 'int'>
max(4, 9, 2)           # built-in function → 9
sum([1, 2, 3])         # built-in function → 6
```

---

## 2. User-Defined Functions

Functions **you write yourself** using the `def` keyword.

```python
def myfunction(x):
    return x + 1

print(myfunction(5))   # 6
```

---

## 3. Lambda Functions (Anonymous Functions)

A short, one-line function without a name, defined using the `lambda` keyword.

```python
square = lambda x: x * x
print(square(5))   # 25
```

**Common use — inside `sorted()`:**
```python
students = [("Sarah", 88), ("Raj", 45), ("Aisha", 72)]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# [('Raj', 45), ('Aisha', 72), ('Sarah', 88)]
```

---

## 4. Functions with Default Arguments

A function can have default values, used only when the caller doesn't provide one.

```python
def greetme(name="ashwini"):
    return f"hello, {name}!"

print(greetme())            # hello, ashwini!
print(greetme("reyansh"))   # hello, reyansh!
```

---

## 5. Functions with Variable Number of Arguments (`*args`, `**kwargs`)

Used when you don't know in advance how many arguments will be passed in.

### `*args` — accepts any number of positional arguments (as a tuple)

```python
def number(*num):
    return sum(num)

print(number(1, 2, 3, 4, 5))   # 15
```

### `**kwargs` — accepts any number of named/keyword arguments (as a dictionary)

```python
def print_profiles(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_profiles(name="Ashwini", age=19, city="Delhi")
```
Output:
```
name: Ashwini
age: 19
city: Delhi
```

---

## 6. Recursive Functions

A function that **calls itself** to solve a smaller version of the same problem, until it hits a stopping point (the **base case**).

```python
def factorial(n):
    if n == 1:                     # base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))   # 120
```

---

## 7. Higher-Order Functions

A function that **takes another function as input**, or **returns a function as output**.

```python
def apply_twice(func, value):
    return func(func(value))

def add_three(x):
    return x + 3

print(apply_twice(add_three, 10))   # 16
```

---

## Quick Summary Table

| Function Type | Example | When to use |
|---|---|---|
| Built-in | `len()`, `print()`, `sum()` | Common, ready-made operations |
| User-defined | `def myfunction(x): return x + 1` | Your own custom logic |
| Lambda | `lambda x: x * x` | Quick, one-line, throwaway logic |
| Default arguments | `def greetme(name="ashwini"):` | Optional parameters with fallback values |
| `*args` | `def number(*num):` | Unknown number of positional inputs |
| `**kwargs` | `def print_profiles(**details):` | Unknown number of named/keyword inputs |
| Recursive | `def factorial(n): ... factorial(n-1)` | Problems that break into smaller versions of themselves |
| Higher-order | `apply_twice(func, value)` | Functions that use other functions as building blocks |

---

## Why This Matters for ML

- **User-defined functions** structure every data-cleaning step and model-building block.
- **Lambda functions** show up constantly in Pandas, e.g., `data["price"].apply(lambda x: x * 1.1)`.
- **`*args` / `**kwargs`** appear in nearly every ML library's function signatures (e.g., `model.fit(X, y, **kwargs)`).
- **Higher-order functions** power common tools like `.apply()`, `.map()`, and `sorted()` in data processing.