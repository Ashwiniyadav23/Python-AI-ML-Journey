# Python Basics — README

Reference notes for **Variables** and **Operators** in Python, with simple examples.

---

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

| Type | Example | Description |
|---|---|---|
| `int` | `age = 25` | Whole number |
| `float` | `height = 5.6` | Decimal number |
| `str` | `name = "Sarah"` | Text (string) |
| `bool` | `is_active = True` | True/False value |

```python
age = 25            # int
height = 5.6        # float
name = "Sarah"      # str
is_active = True    # bool
```

You can check a variable's type using `type()`:

```python
print(type(age))   # <class 'int'>
```

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

