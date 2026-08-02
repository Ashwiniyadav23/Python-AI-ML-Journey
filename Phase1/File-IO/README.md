# 📂 Python File I/O & Error Handling

## 1. File I/O (Input/Output)

File I/O is used to **read data from** and **write data to** files.

### File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read a file |
| `w` | Write (create/overwrite) |
| `a` | Append data |
| `x` | Create a new file |

### Write to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello, Python!")
```

### Read from a File

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

### Common Methods

- `read()` → Read entire file
- `readline()` → Read one line
- `readlines()` → Read all lines as a list
- `write()` → Write data to a file

**Why it matters:** Used to load datasets, save logs, and store application data.

---

# ⚠️ Error Handling (`try` / `except`)

Error handling prevents your program from crashing when an error occurs.

### Syntax

```python
try:
    # Code that may cause an error
except ErrorType:
    # Handle the error
```

### Example

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Common Exceptions

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid input |
| `TypeError` | Wrong data type |
| `FileNotFoundError` | File not found |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |

### `else` and `finally`

```python
try:
    print("No Error")
except:
    print("Error")
else:
    print("Executed if no error")
finally:
    print("Always executes")
```

**Why it matters:** Makes programs reliable by handling unexpected errors gracefully.

---

## 📌 Key Takeaways

- **File I/O** → Read and write data using files.
- **`with open()`** → Opens and automatically closes files.
- **`try/except`** → Handles errors without crashing the program.
- These concepts are essential for Python, Backend Development, and Machine Learning.