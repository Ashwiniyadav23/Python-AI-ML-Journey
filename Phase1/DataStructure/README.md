# Python Data Structures — README

Reference notes on **List**, **Dictionary**, **Tuple**, and **Set** in Python, with examples.

---

## 1. List — An Ordered, Changeable Collection

Lists store multiple items in a specific order, and allow duplicates. You can add, remove, or update items anytime.

```python
arr = [1, 2, 3, 4, 5]
print(arr[0])       # 1  → access the first item (index starts at 0)

arr.append(100)     # adds 100 to the end → [1, 2, 3, 4, 5, 100]
arr[2] = 20          # updates the item at index 2 → [1, 2, 20, 4, 5, 100]
arr.remove(4)        # removes the value 4 (not index 4) → [1, 2, 20, 5, 100]

print(arr)           # [1, 2, 20, 5, 100]
```

**Key things to remember:**
- `arr[index]` → access an item by position (starts at `0`)
- `.append(value)` → adds an item to the end
- `arr[index] = value` → updates an item at a specific position
- `.remove(value)` → removes the **first matching value**, not a position

---

## 2. Dictionary (dict) — Labeled Data

A dictionary stores data as **key–value pairs**, like a mini record with labeled fields. Here it's used inside a list, so you have a list of dictionaries — a very common shape for real datasets (each dictionary = one row/record).

```python
students = [
    {"name": "Ashwini", "age": 19, "grade": 89}
]

print(students)          # Print the entire list
# [{'name': 'Ashwini', 'age': 19, 'grade': 89}]

print(students[0])       # Access the first dictionary (student) from the list
# {'name': 'Ashwini', 'age': 19, 'grade': 89}

print(students[0]["age"])   # Access a specific value using its key
# 19

students[0]["age"] = 20     # Update the value of the "age" key
print(students)
# [{'name': 'Ashwini', 'age': 20, 'grade': 89}]

del students[0]["grade"]    # Delete the "grade" key from the first student's dictionary
print(students)
# [{'name': 'Ashwini', 'age': 20}]
```

**Key things to remember:**
- `list[0]` → gets the first dictionary out of the list
- `dict["key"]` → gets the value for that key
- `dict["key"] = new_value` → updates that key's value
- `del dict["key"]` → permanently removes that key (and its value) from the dictionary

---

## 3. Tuple — Like a List, But Locked (Immutable)

A tuple is ordered like a list, but once created, its values **cannot** be changed, added, or removed. Good for fixed data that should never accidentally be modified.

```python
coordinates = (1, 2, 3, 4, 5, 6, 7)   # e.g. latitude, longitude

# Accessing Elements
result = coordinates[0]
print(result)              # 1

# Negative Indexing
print(coordinates[-1])     # 7   → -1 means "the last element"

# Slicing
print(coordinates[1:4])    # (2, 3, 4)  → items from index 1 up to (not including) index 4
```

**Key things to remember:**
- `tuple[index]` → access by position, same as a list
- `tuple[-1]` → negative indexing counts from the end (`-1` = last item, `-2` = second-last, etc.)
- `tuple[start:stop]` → **slicing** — grabs a range of items; the `stop` index itself is **not included**
- Unlike a list, there's no `.append()`, `.remove()`, or item reassignment — tuples are immutable

---

## 4. Set — Unique Items Only

A set stores items with **no duplicates** and **no guaranteed order**. If you add a duplicate, it's silently ignored.

```python
unique_words = {"hello", "world", "hello"}
print(unique_words)   # {"hello", "world"} — duplicate removed automatically
```

**Key things to remember:**
- Curly braces `{}` define a set (same symbol as a dict, but no key–value pairs)
- Duplicates are automatically dropped
- Order is not guaranteed — don't rely on a set staying in the order you typed it

---

## Quick Comparison Table

| Structure | Ordered? | Changeable? | Duplicates Allowed? | Access By |
|---|---|---|---|---|
| **List** | ✅ Yes | ✅ Yes | ✅ Yes | Index (`arr[0]`) |
| **Dict** | ✅ Yes (insertion order) | ✅ Yes | Keys must be unique | Key (`dict["key"]`) |
| **Tuple** | ✅ Yes | ❌ No | ✅ Yes | Index (`tup[0]`) |
| **Set** | ❌ No | ✅ Yes (add/remove items) | ❌ No | No direct indexing |

---

## Why This Matters for ML

- **Lists** are how you'll store collections of results, predictions, or data points before turning them into a table.
- **Dictionaries** are exactly how a single row of data (a record) is often represented before it becomes part of a Pandas DataFrame — and how API/JSON responses are structured.
- **Tuples** are used for fixed, unchangeable values — e.g., image dimensions `(height, width)`, or coordinates that shouldn't be accidentally modified mid-program.
- **Sets** are useful for quickly finding unique values — e.g., "what are all the distinct categories in this column?" — and for fast membership checks (`if x in my_set`).