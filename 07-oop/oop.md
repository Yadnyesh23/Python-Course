# Object Oriented Programming (OOP) in Python

## What is OOP?

Object Oriented Programming is a programming paradigm that organises code around **objects** — bundles of data (attributes) and behaviour (methods) — rather than writing a series of procedures or functions.

Everything in Python is an object — integers, strings, lists, functions. OOP lets you create your **own custom types** using classes.

```python
# Without OOP — scattered, hard to manage
name1   = "Masala Chai"
price1  = 40
name2   = "Ginger Chai"
price2  = 50

# With OOP — organised, reusable
class Chai:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

masala = Chai("Masala Chai", 40)
ginger = Chai("Ginger Chai", 50)
```

---

## Why Do We Need OOP?

- **Organisation** — groups related data and behaviour together in one place
- **Reusability** — write a class once, create as many objects as needed
- **Modularity** — each class is a self-contained unit, easy to update without breaking others
- **Abstraction** — hide complex implementation, expose only what's needed
- **Real-world modelling** — objects map naturally to real things (a User, a Product, an Order)

---

## Core Concepts of OOP

| Concept | Meaning |
|---------|---------|
| **Class** | Blueprint/template for creating objects |
| **Object** | An instance of a class |
| **Attribute** | Data stored in an object |
| **Method** | Function defined inside a class |
| **`__init__`** | Constructor — runs automatically when an object is created |
| **`self`** | Reference to the current object instance |

---

## Class and Object

A **class** is the blueprint. An **object** is a specific instance created from that blueprint.

```python
# Creating a class
class Chai:
    pass   # empty class — valid Python

# Creating objects (instances)
ginger_tea = Chai()
masala_tea = Chai()

print(type(ginger_tea))   # <class '__main__.Chai'>
print(ginger_tea)         # <__main__.Chai object at 0x...>
```

> `ginger_tea` and `masala_tea` are two separate objects — both made from the same `Chai` blueprint, but completely independent.

---

## The `__init__` Method (Constructor)

`__init__` runs automatically when an object is created. It initialises the object's attributes.

```python
class Chai:
    def __init__(self, name, price, is_hot=True):
        self.name   = name     # instance attribute
        self.price  = price
        self.is_hot = is_hot

# Creating objects
masala = Chai("Masala Chai", 40)
iced   = Chai("Iced Lemon Tea", 60, is_hot=False)

print(masala.name)    # Masala Chai
print(iced.price)     # 60
print(iced.is_hot)    # False
```

---

## `self`

`self` is a reference to the **current instance** of the class. It connects attributes and methods to the specific object being used.

```python
class Chai:
    def __init__(self, name, price):
        self.name  = name   # belongs to THIS object
        self.price = price

masala = Chai("Masala Chai", 40)
ginger = Chai("Ginger Chai", 50)

print(masala.name)   # Masala Chai  ← masala's own name
print(ginger.name)   # Ginger Chai  ← ginger's own name
```

> `self` is just a convention — you could name it anything, but `self` is the universal Python standard.

---

## Instance Methods

Methods are functions defined inside a class. They always take `self` as the first parameter.

```python
class Chai:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def describe(self):
        print(f"{self.name} costs ₹{self.price}")

    def apply_discount(self, percent):
        self.price = round(self.price * (1 - percent / 100), 2)
        print(f"Discounted price of {self.name}: ₹{self.price}")

masala = Chai("Masala Chai", 40)
masala.describe()           # Masala Chai costs ₹40
masala.apply_discount(10)   # Discounted price of Masala Chai: ₹36.0
```

---

## Class Attributes vs Instance Attributes

**Instance attributes** are unique to each object. **Class attributes** are shared across all objects of that class.

```python
class Chai:
    category = "Hot Beverage"   # class attribute — shared by all

    def __init__(self, name, price):
        self.name  = name    # instance attribute — unique to each object
        self.price = price

masala = Chai("Masala Chai", 40)
ginger = Chai("Ginger Chai", 50)

print(masala.category)   # Hot Beverage  ← from class
print(ginger.category)   # Hot Beverage  ← same shared value
print(masala.name)       # Masala Chai   ← masala's own
print(ginger.name)       # Ginger Chai   ← ginger's own

# Changing class attribute affects all instances
Chai.category = "Beverage"
print(masala.category)   # Beverage
print(ginger.category)   # Beverage
```

---

## Class and Object Namespace

Every class and every object has its own **namespace** — a dictionary of names it knows about. Understanding namespaces explains how Python looks up attributes.

```python
class Chai:
    origin = "India"   # class-level attribute — lives in Chai's namespace

print(Chai.origin)     # India

# You can add new attributes to the class dynamically
Chai.is_hot = True

print(Chai.origin)     # India
print(Chai.is_hot)     # True
```

### Instance namespace vs class namespace

When you access an attribute on an object, Python first looks in the **instance namespace**, then falls back to the **class namespace**.

```python
masala_tea = Chai()

print(f"Masala origin : {masala_tea.origin}")    # India  ← from class namespace
print(f"Masala is_hot : {masala_tea.is_hot}")    # True   ← from class namespace

# Now set is_hot on the instance — creates an entry in the INSTANCE namespace
masala_tea.is_hot = False

print(f"Masala is_hot : {masala_tea.is_hot}")    # False  ← from instance namespace (shadows class)
print(f"Class is_hot  : {Chai.is_hot}")          # True   ← class namespace unchanged
```

### The lookup chain

```
obj.attr
  → 1. Check instance namespace  (obj.__dict__)
  → 2. Check class namespace     (ClassName.__dict__)
  → 3. Check parent classes      (MRO — Method Resolution Order)
  → 4. AttributeError if not found
```

```python
# Inspect namespaces directly
class Chai:
    origin = "India"

    def __init__(self, name):
        self.name = name

masala = Chai("Masala Chai")

print(Chai.__dict__)    # {'origin': 'India', '__init__': <function>, ...}
print(masala.__dict__)  # {'name': 'Masala Chai'}
```

> When you do `masala_tea.is_hot = False`, Python creates a **new entry in the instance's namespace**. It doesn't modify the class attribute — it shadows it. The class's `is_hot` remains `True`.

---

## The Four Pillars of OOP

### 1. Encapsulation
Bundling data and methods together, and **restricting direct access** to internal details.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner     = owner
        self.__balance = balance   # __ makes it private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance      # controlled access via a method

account = BankAccount("Yadnyesh", 5000)
account.deposit(1000)
print(account.get_balance())    # 6000
# print(account.__balance)      # ❌ AttributeError — can't access directly
```

| Access Modifier | Syntax | Accessible From |
|----------------|--------|----------------|
| Public | `self.name` | Anywhere |
| Protected | `self._name` | Class + subclasses (by convention) |
| Private | `self.__name` | Only within the class |

---

### 2. Inheritance
A class can **inherit** attributes and methods from another class, avoiding duplication.

```python
class Beverage:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def describe(self):
        print(f"{self.name} costs ₹{self.price}")

class Chai(Beverage):           # Chai inherits from Beverage
    def __init__(self, name, price, spice_level):
        super().__init__(name, price)   # call parent's __init__
        self.spice_level = spice_level

    def describe(self):                 # override parent method
        super().describe()
        print(f"Spice level: {self.spice_level}")

masala = Chai("Masala Chai", 40, "High")
masala.describe()
```

**Output:**
```
Masala Chai costs ₹40
Spice level: High
```

> `super()` gives access to the parent class. Use it to call the parent's `__init__` or any overridden method.

---

### 3. Polymorphism
The same method name behaves **differently** depending on the object calling it.

```python
class Chai:
    def prepare(self):
        print("Boiling milk, adding spices...")

class Coffee:
    def prepare(self):
        print("Grinding beans, pulling espresso...")

class GreenTea:
    def prepare(self):
        print("Steeping leaves in hot water...")

drinks = [Chai(), Coffee(), GreenTea()]

for drink in drinks:
    drink.prepare()   # each calls its own version
```

**Output:**
```
Boiling milk, adding spices...
Grinding beans, pulling espresso...
Steeping leaves in hot water...
```

---

### 4. Abstraction
Hiding complex implementation details and **exposing only what's necessary**.

```python
from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def prepare(self):
        pass   # subclasses MUST implement this

    def serve(self):
        self.prepare()
        print("Served!")

class Chai(Beverage):
    def prepare(self):
        print("Masala Chai is ready")

class Coffee(Beverage):
    def prepare(self):
        print("Espresso is ready")

chai = Chai()
chai.serve()
# Masala Chai is ready
# Served!

# Beverage()   # ❌ TypeError — cannot instantiate abstract class
```

---

## Special (Dunder) Methods

Special methods (double underscore — "dunder") let your objects integrate with Python's built-in operations like `print()`, `len()`, `+`, `==`, and so on.

```python
class Chai:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def __str__(self):
        return f"{self.name} — ₹{self.price}"       # used by print()

    def __repr__(self):
        return f"Chai('{self.name}', {self.price})"  # used in console/debugging

    def __eq__(self, other):
        return self.price == other.price             # == operator

    def __lt__(self, other):
        return self.price < other.price              # < operator

    def __add__(self, other):
        return self.price + other.price              # + operator

    def __len__(self):
        return len(self.name)                        # len() function

masala = Chai("Masala Chai", 40)
ginger = Chai("Ginger Chai", 50)

print(masala)              # Masala Chai — ₹40
print(repr(masala))        # Chai('Masala Chai', 40)
print(masala == ginger)    # False
print(masala < ginger)     # True
print(masala + ginger)     # 90
print(len(masala))         # 11
```

| Dunder Method | Triggered by |
|--------------|-------------|
| `__init__` | `ClassName()` |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | `repr(obj)`, console display |
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__add__` | `+` |
| `__len__` | `len(obj)` |
| `__del__` | object is garbage collected |
| `__contains__` | `in` operator |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = value` |

---

## Class Methods and Static Methods

```python
class Chai:
    total_chais = 0   # class attribute

    def __init__(self, name):
        self.name = name
        Chai.total_chais += 1

    @classmethod
    def get_total(cls):
        return f"Total chais created: {cls.total_chais}"

    @staticmethod
    def is_caffeinated(chai_type):
        return chai_type.lower() not in ["herbal", "rooibos"]

print(Chai.get_total())                  # Total chais created: 0
masala = Chai("Masala Chai")
ginger = Chai("Ginger Chai")
print(Chai.get_total())                  # Total chais created: 2
print(Chai.is_caffeinated("Herbal"))     # False
print(Chai.is_caffeinated("Masala"))     # True
```

| Method Type | Decorator | First Parameter | Access |
|-------------|-----------|----------------|--------|
| Instance method | none | `self` | Instance + class data |
| Class method | `@classmethod` | `cls` | Class data only |
| Static method | `@staticmethod` | none | Neither — utility function |

---

## Quick Reference

```python
# Define a class
class MyClass:
    class_attr = "shared"             # class attribute

    def __init__(self, value):
        self.value = value            # instance attribute

    def instance_method(self):        # instance method
        return self.value

    @classmethod
    def class_method(cls):            # class method
        return cls.class_attr

    @staticmethod
    def static_method():              # static method
        return "no self or cls"

    def __str__(self):                # string representation
        return f"MyClass({self.value})"

# Create an object
obj = MyClass("hello")
print(obj)                            # MyClass(hello)
print(obj.instance_method())          # hello
print(MyClass.class_method())         # shared
print(MyClass.static_method())        # no self or cls

# Inspect namespaces
print(MyClass.__dict__)               # class namespace
print(obj.__dict__)                   # instance namespace
```

## Attribute Shadowing