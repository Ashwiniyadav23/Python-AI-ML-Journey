# Virtual Environments & Package Managers (`pip` / `conda`) 

Reference notes on installing packages and managing isolated project environments in Python.

---

## Why Virtual Environments Exist

Imagine:
- **Project A** needs `pandas` version 1.0
- **Project B** needs `pandas` version 2.0

If you install packages globally (system-wide), installing version 2.0 for Project B **overwrites** version 1.0 — breaking Project A.

A **virtual environment** creates an isolated, separate "box" of installed packages for each project, so they never conflict with each other.

---

## 1. `pip` — Python's Package Installer

`pip` installs third-party packages from **PyPI** (Python Package Index), the official repository of Python packages.

```bash
pip install pandas              # install a package
pip install pandas==1.5.3       # install a specific version
pip install pandas numpy scipy  # install multiple at once
pip uninstall pandas            # remove a package
pip list                        # see everything installed
pip show pandas                 # see details about one package
```

**Key things to remember:**
- `pip install <package>` → gets the latest version
- `pip install <package>==<version>` → pins an exact version (important for reproducibility)
- `pip list` and `pip show` are useful for checking what's already installed and its version

---

## 2. Creating a Virtual Environment with `venv` (Built into Python)

`venv` is Python's built-in tool for creating isolated environments — no separate installation needed.

```bash
python -m venv myenv          # creates a folder called "myenv" — your isolated environment
```

### Activating the environment

```bash
# On Mac/Linux:
source myenv/bin/activate

# On Windows:
myenv\Scripts\activate
```

Once activated, your terminal prompt usually shows the environment name, like `(myenv) $`. From this point, anything you install only affects **this** environment.

```bash
(myenv) $ pip install pandas    # installed only inside myenv
```

### Exiting the environment

```bash
deactivate                       # exit the environment when done
```

**Key things to remember:**
- Always activate the environment *before* running `pip install` for a specific project
- `deactivate` returns you to your system's global Python — nothing from `myenv` follows you out

---

## 3. `conda` — An Alternative Environment/Package Manager

`conda` (from Anaconda/Miniconda) manages both environments *and* packages — and unlike `venv`, it can also install a specific **Python version** itself, plus manage non-Python dependencies that some data science packages rely on.

```bash
conda create --name myenv python=3.11    # create an environment with a specific Python version
conda activate myenv                      # activate it
conda install pandas numpy                # install packages
conda deactivate                          # exit the environment
conda env list                            # see all environments you've created
```

**Key things to remember:**
- `conda create --name <env_name> python=<version>` → creates the environment AND sets the Python version in one step
- `conda activate` / `conda deactivate` → same idea as `venv`'s activate/deactivate, different command
- `conda env list` → lets you see every environment you've ever created, so you don't lose track

---

## Quick Comparison Table

| | `pip` + `venv` | `conda` |
|---|---|---|
| Installs packages from | PyPI | Anaconda repository (can also use pip) |
| Creates isolated environments | ✅ Yes (`venv`) | ✅ Yes |
| Can set/manage Python version itself | ❌ No | ✅ Yes |
| Comes with | Every Python install | Anaconda/Miniconda installer |
| Best for | Lightweight, general Python projects | Data science stacks with complex dependencies |

---

## Requirements Files — Sharing Your Setup with Others

Once your environment is set up, you can save exactly what's installed:

```bash
pip freeze > requirements.txt
```

This creates a file listing every package and version:
```
pandas==2.1.0
numpy==1.26.0
scikit-learn==1.3.0
```

Anyone else (or you, on a new computer) can recreate the exact same environment with:
```bash
pip install -r requirements.txt
```

This is why almost every GitHub ML project includes a `requirements.txt` — it's the recipe for recreating the exact toolbox that project needs.

---

## Why This Matters for ML

- Every ML project you build should live in its **own environment**, so its exact package versions are locked in and reproducible.
- Sharing a `requirements.txt` (or a `conda` environment file) means a teammate — or your future self — can recreate your exact setup with one command, instead of guessing which versions you used.
- `conda` is especially common in ML/data science because some packages (e.g. those relying on GPU libraries) are easier to install correctly through conda than through pip alone.