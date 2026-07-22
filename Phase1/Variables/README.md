

# 📌 SECTION 1: Variables

## What is a Variable?

A variable is a **labeled box** that stores a value in memory, so you can use or change it later.

```python
age = 25
name = "Sarah"
```

Here, `age` and `name` are variables. You give them a name once, and can reuse or update them anytime.

## Declaring a Variable

Python doesn't require you to specify a type — it figures it out automatically.

```python
x = 10          # Python knows this is a number
y = "hello"     # Python knows this is text
```

## Data Types

Python has several built-in data types. They generally fall into two groups:
- **Basic / single-value types** — store one value at a time
- **Collection types** — store multiple values together

### Basic Types

| Type | Example | Description |
|---|---|---|
| `int` | `age = 25` | Whole number |
| `float` | `height = 5.6` | Decimal number |
| `str` | `name = "Sarah"` | Text (string) |
| `bool` | `is_active = True` | True/False value |
| `complex` | `z = 3 + 4j` | Number with a real and imaginary part (rarely used outside math/engineering) |
| `NoneType` | `result = None` | Represents "nothing" or "no value yet" |

```python
age = 25            # int
height = 5.6        # float
name = "Sarah"      # str
is_active = True    # bool
z = 3 + 4j          # complex
result = None       # NoneType
```

**`None` deserves a closer look** — it's Python's way of saying "empty" or "not set yet," different from `0` or `""` (empty string).

```python
score = None            # no score recorded yet

if score is None:
    print("No score entered yet")
else:
    print(f"Score: {score}")
```

You'll see `None` constantly in ML code — e.g., a function that hasn't returned a value yet, or a missing value in a dataset before it's cleaned.

You can check a variable's type using `type()`:

```python
print(type(age))   # <class 'int'>
print(type(result))   # <class 'NoneType'>
```

### Collection Types — storing multiple values

| Type | Example | Description |
|---|---|---|
| `list` | `scores = [85, 90, 78]` | Ordered, changeable collection (allows duplicates) |
| `tuple` | `point = (28.6, 77.2)` | Ordered, but CANNOT be changed after creation |
| `dict` | `person = {"name": "Sarah", "age": 21}` | Key–value pairs (like a labeled mini-database) |
| `set` | `unique = {1, 2, 2, 3}` | Unordered, automatically removes duplicates |

```python
# list — ordered, changeable
scores = [85, 90, 78]
scores.append(100)
print(scores)          # [85, 90, 78, 100]

# tuple — ordered, unchangeable
point = (28.6, 77.2)
# point[0] = 30       # ❌ this would cause an error — tuples can't be edited

# dict — key-value pairs
person = {"name": "Sarah", "age": 21}
print(person["name"])  # Sarah

# set — no duplicates allowed
unique = {1, 2, 2, 3, 3, 3}
print(unique)           # {1, 2, 3}
```

**Why so many collection types?** Each solves a different problem:
- Use a **list** when order matters and you'll add/remove items (e.g., a growing list of scores)
- Use a **tuple** when the data shouldn't change (e.g., fixed GPS coordinates)
- Use a **dict** when you need labeled fields (e.g., one row of a dataset: name, age, score)
- Use a **set** when you just need unique items and don't care about order (e.g., removing duplicate words from text)

### Checking and Converting Types

You can convert between types using `int()`, `float()`, `str()`, `bool()`, `list()`, etc.

```python
x = "25"
y = int(x)          # converts string "25" to integer 25
print(y + 5)        # 30

z = str(100)        # converts integer 100 to string "100"
print(z + "%")       # "100%"
```

This matters a lot in real data — numbers loaded from a CSV file sometimes arrive as text (`"25"` instead of `25`), and you need to convert them before doing math on them.

## Updating a Variable

```python
score = 10
score = score + 5    # score is now 15
print(score)         # 15
```

Shortcut for the same thing:

```python
score += 5   # same as score = score + 5
score -= 2   # same as score = score - 2
score *= 3   # same as score = score * 3
score /= 2   # same as score = score / 2
```

## Multiple Assignment

```python
x, y, z = 1, 2, 3
print(x, y, z)   # 1 2 3
```

## Naming Rules

- Must start with a letter or underscore (`_`), not a number
- Can contain letters, numbers, underscores
- Case-sensitive (`age` and `Age` are different variables)
- Cannot use Python reserved keywords (`if`, `for`, `class`, etc.)

```python
user_name = "Sarah"     # ✅ valid
_temp = 10               # ✅ valid
2fast = "no"             # ❌ invalid — starts with a number
```

## Variables in Practice — Example

```python
name = "Sarah"
age = 21
gpa = 3.8

print(f"{name} is {age} years old with a GPA of {gpa}")
# Output: Sarah is 21 years old with a GPA of 3.8
```

## Why Variables Matter in ML

Every dataset column, every model weight, every prediction is stored in a variable. Understanding how values are stored and updated is the foundation for everything that follows — including how a model's "weights" get updated during training.
