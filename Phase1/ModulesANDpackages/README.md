# Python Modules & `import` Mechanics 

Reference notes on **modules**, **packages**, and the different ways to `import` code in Python.

---

## What is a Module?

A **module** is simply a Python file (`.py`) containing code — functions, classes, variables — that you can reuse in other files.

**Example — creating your own module.** Save this in a file called `math_utils.py`:

```python
# math_utils.py

def add(a, b):
    return a + b

def square(x):
    return x * x

PI = 3.14159
```

Now, in a different file (e.g. `main.py`), you can **import** and use it:

```python
import math_utils

print(math_utils.add(2, 3))      # 5
print(math_utils.square(4))      # 16
print(math_utils.PI)             # 3.14159
```

You just reused code from another file instead of rewriting it.

---

## Different Ways to Import

```python
import math_utils                     # import the whole module
print(math_utils.add(2, 3))           # 5

from math_utils import add            # import just one function
print(add(2, 3))                      # 5

from math_utils import add, square    # import multiple specific things
print(add(2, 3))                      # 5
print(square(4))                      # 16

from math_utils import add as sum_two_numbers   # rename on import ("alias")
print(sum_two_numbers(2, 3))          # 5

import math_utils as mu               # alias the whole module (very common!)
print(mu.add(2, 3))                   # 5
```

### When to use which style

| Style | Example | When to use |
|---|---|---|
| `import module` | `import math_utils` | When you'll use several things from the module — access each with `module.name` |
| `from module import thing` | `from math_utils import add` | When you only need one or two specific things, and want to call them directly (`add(...)` instead of `math_utils.add(...)`) |
| `import module as alias` | `import math_utils as mu` | To shorten a long module name you'll type often |
| `from module import thing as alias` | `from math_utils import add as sum_two_numbers` | To rename something for clarity, or to avoid a naming clash with your own code |

---

## Third-Party Modules/Packages (Need Installation)

Things like `pandas`, `numpy`, and `torch` aren't built into Python — you install them separately (via `pip` or `conda`), then import them the exact same way as your own modules:

```python
import pandas as pd

data = pd.read_csv("data.csv")
```

Here, `pd` is just an alias for `pandas` — the same aliasing idea shown above (`import math_utils as mu`), just applied to a very well-known, widely used package. Using `pd` as the alias for pandas (and `np` for numpy) is such a strong convention that virtually every Python data project follows it.

---

## What is a Package?

A **package** is just a **folder** containing multiple related modules, organized together. Think of it as: module = one file, package = a folder of files (which may even contain sub-folders of more modules).

```
my_project/
│
├── data_tools/          ← this folder is a package
│   ├── __init__.py       ← (marks this folder as a package)
│   ├── cleaning.py       ← a module inside the package
│   └── visualization.py  ← another module inside the package
│
└── main.py
```

```python
from data_tools import cleaning
cleaning.remove_duplicates(my_data)

# or, importing a specific function directly:
from data_tools.cleaning import remove_duplicates
remove_duplicates(my_data)
```

`pandas`, `numpy`, and `sklearn` are all just packages — folders full of organized modules — that someone else built and published for you to install and import.

---

## Built-in Modules (No Installation Needed)

Python comes with many modules pre-installed, called the **standard library**:

```python
import math
print(math.sqrt(16))   # 4.0

import random
print(random.randint(1, 10))   # a random number between 1 and 10

import datetime
print(datetime.date.today())   # today's date
```

---

## How Python Actually Finds What You're Importing

When you write `import math_utils`, Python searches, in this order:
1. The current folder you're running your script from
2. A list of "installed" locations (where `pip` installs packages)
3. Python's built-in standard library locations

If it's not found in any of these, you get:
```
ModuleNotFoundError: No module named 'math_utils'
```

This is one of the most common beginner errors — it usually means either a typo, the file is in the wrong folder, or the package was never installed.

---

## Quick Summary Table

| Term | Meaning | Example |
|---|---|---|
| **Module** | A single reusable `.py` file | `math_utils.py` |
| **Package** | A folder of related modules | `pandas`, `data_tools/` |
| **Standard library** | Built-in modules, no install needed | `math`, `random`, `datetime` |
| **Third-party package** | Needs installing via `pip`/`conda` | `pandas`, `numpy`, `torch` |
| **Alias** | A shorter/renamed reference on import | `import pandas as pd` |

---

## Why This Matters for ML

- Almost every ML script starts with a block of imports (`pandas`, `numpy`, `sklearn`, `torch`) — recognizing these patterns instantly is core to reading any ML codebase.
- Organizing your own project into modules/packages (instead of one giant file) keeps data-cleaning code, model code, and utility functions clean and reusable across notebooks and scripts.
- Aliases like `pd` and `np` are near-universal conventions — using them makes your code instantly familiar to anyone else in the field.