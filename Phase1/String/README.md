# Python String Manipulation 

Reference notes on **String Manipulation** in Python — creating, accessing, joining, changing case, finding, replacing, and formatting strings.

---

## What is String Manipulation?

String manipulation means performing operations on strings, such as:
- Creating strings
- Accessing characters
- Joining strings
- Changing case
- Finding text
- Replacing text
- Formatting strings

---

## 1. Creating Strings

```python
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""

print(s1)   # Hello
print(s2)   # World
print(s3)
```

You can use single quotes, double quotes, or triple quotes (for multi-line text) — Python treats them the same way.

---

## 2. Accessing Characters

Each character in a string has a position (index), starting at `0`.

```python
word = "Python"

print(word[0])    # P   → first character
print(word[3])    # h   → 4th character
print(word[-1])   # n   → last character (negative indexing)
print(word[1:4])  # yth → slicing (index 1 up to, not including, 4)
```

**Key things to remember:**
- Indexing starts at `0`, not `1`
- Negative indexes count from the end (`-1` = last character)
- Slicing `[start:stop]` includes `start` but excludes `stop`

---

## 3. Joining Strings

```python
first = "Hello"
second = "World"

combined = first + " " + second
print(combined)   # Hello World

words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)   # I love Python
```

`" ".join(words)` means: "join all items in the list using a space as the separator." You can join with any separator, e.g. `"-".join(words)` → `I-love-Python`.

---

## 4. Changing Case

```python
text = "Hello World"

print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World  (capitalizes each word)
print(text.capitalize()) # Hello world  (capitalizes only the first letter)
```

---

## 5. Finding Text

```python
sentence = "I love learning Python"

print(sentence.find("learning"))    # 7   → starting index where "learning" begins
print("Python" in sentence)         # True  → checks if the text exists at all
print(sentence.count("o"))          # 3   → counts how many times "o" appears
```

`.find()` returns `-1` if the text isn't found at all:
```python
print(sentence.find("Java"))   # -1
```

---

## 6. Replacing Text

```python
sentence = "I love Java"

updated = sentence.replace("Java", "Python")
print(updated)   # I love Python
```

---

## 7. Formatting Strings

The modern, cleanest way is an **f-string** — insert variables directly into text.

```python
name = "Ashwini"
age = 19

message = f"My name is {name} and I am {age} years old."
print(message)   # My name is Ashwini and I am 19 years old.
```

You can even do calculations inside an f-string:
```python
price = 500
tax = 0.18

print(f"Total price: {price + (price * tax)}")   # Total price: 590.0
```

---

## Quick Summary Table

| Operation | Method/Syntax | Example Result |
|---|---|---|
| Create | `"text"`, `'text'`, `"""multi-line"""` | `Hello` |
| Access | `s[index]`, `s[-1]`, `s[start:stop]` | `P`, `n`, `yth` |
| Join | `+`, `" ".join(list)` | `Hello World`, `I love Python` |
| Change case | `.upper()`, `.lower()`, `.title()` | `HELLO`, `hello`, `Hello World` |
| Find | `.find()`, `in`, `.count()` | index, `True`/`False`, count |
| Replace | `.replace(old, new)` | `I love Python` |
| Format | f-strings `f"{variable}"` | `My name is Ashwini` |

---

## Why This Matters for ML

- **Cleaning text data** almost always uses `.lower()`, `.strip()`, and `.replace()` to standardize messy text before analysis.
- **Finding/counting text** is core to basic NLP tasks, like counting word frequency or checking for keywords.
- **f-strings** are the standard way to build readable print statements, log messages, and labels for charts/results.
- **Joining strings** is used when combining tokens (words) back into sentences, e.g., after processing text for a model.