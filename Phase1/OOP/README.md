# Python OOP (Object-Oriented Programming) 

Reference notes on **Classes**, **Encapsulation**, **Inheritance**, **Abstraction**, and **Polymorphism** in Python, with examples.

---

## 1. Classes & Objects — The Basic Blueprint

A **class** is a blueprint. An **object** is a real "thing" built from that blueprint, with its own data.

```python
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):       # Method to display the student's details
        print(f"Name: {self.name} Marks: {self.marks}")

s1 = Students("Ashwini", 95)
s1.display()
```
Output:
```
Name: Ashwini Marks: 95
```

**Key things to remember:**
- `__init__` is the **constructor** — it runs automatically when you create an object, setting up its initial data
- `self` refers to "this specific object" — it's how the object accesses its own data (`self.name`, `self.marks`)
- `s1 = Students("Ashwini", 95)` creates an actual object (an "instance") from the `Students` blueprint

---

## 2. Encapsulation — Keeping Data and Methods Together in One Class

Encapsulation means bundling related data (variables) and behavior (methods) inside a single class, so they travel together as one unit.

```python
class Students:
    def __init__(self, name, marks, roll):
        self.name = name
        self.marks = marks
        self.roll = roll

    def display(self):
        print(f"Name: {self.name} Marks: {self.marks} Roll-no: {self.roll}")

s1 = Students("Ashwini", 89, 20)
s1.display()
```
Output:
```
Name: Ashwini Marks: 89 Roll-no: 20
```

> ⚠️ **Fixes made from the original snippet:**
> 1. `s1 = (name:"Ashwini", Marks:89, roll:20)` is not valid Python syntax — creating an object always looks like `s1 = Students("Ashwini", 89, 20)`, passing values in order, without naming them with colons.
> 2. Inside `display()`, the original used `name`, `Marks`, `roll` directly — but those are only accessible as `self.name`, `self.Marks`, `self.roll`, since they belong to the object, not the surrounding code.
> 3. `Students.display()` called the method on the **class** itself, with no object and no data to display. You call it on the **object** instead: `s1.display()`.

**Why encapsulation matters:** all of a student's related data (`name`, `marks`, `roll`) and the actions on that data (`display`) live inside one class — instead of scattered loose variables and separate functions that could easily get mismatched.

---

## 3. Inheritance — Reusing Existing Code

Inheritance lets a new class automatically get all the methods and data of an existing class, so you don't have to rewrite them.

```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()
```
Output:
```
Eating...
```

**Key things to remember:**
- `class Dog(Animal):` means "Dog inherits everything from Animal"
- `pass` means "nothing extra to add here" — `Dog` doesn't need its own code to use `eat()`, since it already inherited it
- `Animal` is called the **parent class** (or base class), and `Dog` is the **child class** (or subclass)

**A more useful example — child class adding its own extra method:**
```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()    # inherited from Animal
dog.bark()   # defined in Dog itself
```

---

## 4. Abstraction — Showing Only What's Necessary

Abstraction means hiding the internal detail of *how* something works, and only exposing a simple way to *use* it.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            print("Passed")
        else:
            print("Failed")

s1 = Student("Ashwini", 95)
s1.result()
```
Output:
```
Passed
```

**Why this is "abstraction":** whoever uses `s1.result()` doesn't need to know or care *how* pass/fail is calculated internally (the `if/else` logic) — they just call one simple method and get an answer. The complexity is hidden behind a clean interface.

---

## 5. Polymorphism — One Interface, Many Forms

Polymorphism means different classes can have a method with the **same name**, but each class implements it differently.

```python
class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()   # Woof
cat.sound()   # Meow
```
Output:
```
Woof
Meow
```

**Why this is "polymorphism":** both `Dog` and `Cat` have a method called `sound()` — same name, same "interface" — but each class defines its own version of what actually happens when it's called.

**A more powerful example — using polymorphism in a loop:**
```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```
Output:
```
Woof
Meow
```

You can treat different objects the same way (calling `.sound()` on each) without needing to know or check which exact type each one is — Python figures out the right version to run automatically.

---

## Quick Summary Table

| Concept | What it means | Example from above |
|---|---|---|
| **Class & Object** | A blueprint, and a real "thing" built from it | `Students`, `s1 = Students(...)` |
| **Encapsulation** | Bundling data + methods together in one class | `name`, `marks`, `roll` + `display()` all inside `Students` |
| **Inheritance** | A class reusing another class's code | `Dog(Animal)` inherits `eat()` |
| **Abstraction** | Hiding internal detail behind a simple method | `s1.result()` hides the if/else logic |
| **Polymorphism** | Same method name, different behavior per class | `dog.sound()` vs `cat.sound()` |

---

## Why This Matters for ML

This exact pattern — a class with `__init__` and methods — is precisely how ML models are structured in PyTorch:

```python
class MyModel(nn.Module):        # Inheritance — reusing PyTorch's base Module class
    def __init__(self):
        super().__init__()
        # define layers here    (Encapsulation — layers + logic live together)

    def forward(self, x):
        # define how data flows through the model   (Abstraction — hides the math details)
        return x
```

If the `Students`/`Dog`/`Cat` examples above make sense, PyTorch model code will read as a familiar pattern rather than unfamiliar syntax — it's the same OOP ideas, just applied to neural network layers instead of student records or animal sounds.