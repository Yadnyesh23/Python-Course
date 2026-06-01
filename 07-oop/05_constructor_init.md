# Constructor and `__init__` in Python

## What is a Constructor?

A constructor is a special method that runs **automatically when an object is created**. It sets up the object's initial state — assigning values to attributes so the object is ready to use from the moment it's created.

In Python, the constructor is the `__init__` method.

```python
class ChaiOrder:
    def __init__(self, type_, size):   # runs automatically on object creation
        self.type = type_
        self.size = size
```

> The name `__init__` stands for "initialise". The double underscores mark it as a special Python method (dunder method).

---

## Why Do We Need `__init__`?

Without `__init__`, every object starts empty — you'd have to manually set every attribute after creation, which is repetitive and error-prone.

```python
# Without __init__ — manual setup every time
class Chai:
    pass

masala      = Chai()
masala.type = "Masala"
masala.size = 200

ginger      = Chai()
ginger.type = "Ginger"
ginger.size = 250

# With __init__ — clean, automatic, consistent
class Chai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

masala = Chai("Masala", 200)
ginger = Chai("Ginger", 250)
```

---

## Basic Example

```python
class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order1 = ChaiOrder("Masala", 200)
print(order1.summary())   # 200ml of Masala chai

order2 = ChaiOrder("Lemon", 250)
print(order2.summary())   # 250ml of Lemon chai
```

> `type_` is used instead of `type` because `type` is a **built-in Python function** — using it as a parameter name would shadow it. Adding an underscore is the standard convention.

---

## How `__init__` Works Step by Step

```python
order1 = ChaiOrder("Masala", 200)
```

1. Python creates a new, empty `ChaiOrder` object
2. Python calls `ChaiOrder.__init__(order1, "Masala", 200)` automatically
3. Inside `__init__`, `self.type = "Masala"` and `self.size = 200` are stored on the object
4. The fully initialised object is assigned to `order1`

---

## `__init__` with Default Values

Parameters in `__init__` can have default values, making them optional.

```python
class ChaiOrder:
    def __init__(self, type_="Masala", size=150, is_hot=True):
        self.type   = type_
        self.size   = size
        self.is_hot = is_hot

    def summary(self):
        temp = "Hot" if self.is_hot else "Iced"
        return f"{temp} {self.size}ml {self.type} chai"

order1 = ChaiOrder()                          # all defaults
order2 = ChaiOrder("Ginger")                  # custom type, rest default
order3 = ChaiOrder("Lemon", 300, is_hot=False) # fully custom

print(order1.summary())   # Hot 150ml Masala chai
print(order2.summary())   # Hot 150ml Ginger chai
print(order3.summary())   # Iced 300ml Lemon chai
```

---

## `__init__` with Validation

You can add logic inside `__init__` to validate inputs before storing them.

```python
class ChaiOrder:
    VALID_SIZES = [150, 200, 250, 300]

    def __init__(self, type_, size):
        if size not in self.VALID_SIZES:
            raise ValueError(f"Invalid size {size}ml. Choose from {self.VALID_SIZES}")
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order1 = ChaiOrder("Masala", 200)
print(order1.summary())   # 200ml of Masala chai

# order2 = ChaiOrder("Lemon", 500)   # ❌ ValueError: Invalid size 500ml
```

---

## `__init__` with Computed Attributes

Attributes don't have to come directly from parameters — you can compute them inside `__init__`.

```python
class ChaiOrder:
    PRICE_PER_ML = 0.25   # ₹ per ml

    def __init__(self, type_, size):
        self.type  = type_
        self.size  = size
        self.price = round(size * self.PRICE_PER_ML, 2)   # computed on creation

    def summary(self):
        return f"{self.size}ml {self.type} chai — ₹{self.price}"

order = ChaiOrder("Masala", 200)
print(order.summary())   # 200ml Masala chai — ₹50.0
```

---

## `__init__` vs `__new__`

Python actually has two steps when creating an object:

| Method | Role | Called by |
|--------|------|-----------|
| `__new__` | **Creates** the object (allocates memory) | Python internally |
| `__init__` | **Initialises** the object (sets attributes) | Python after `__new__` |

In everyday Python you only ever use `__init__`. `__new__` is only needed for advanced cases like singleton patterns or immutable types.

```python
class Chai:
    def __new__(cls):
        print("__new__: object created")
        return super().__new__(cls)

    def __init__(self):
        print("__init__: object initialised")

c = Chai()
# __new__: object created
# __init__: object initialised
```

---

## `__del__` — The Destructor

`__del__` is the opposite of `__init__` — it runs when the object is about to be destroyed (garbage collected).

```python
class ChaiOrder:
    def __init__(self, type_):
        self.type = type_
        print(f"Order for {self.type} created")

    def __del__(self):
        print(f"Order for {self.type} completed and removed")

order = ChaiOrder("Masala")   # Order for Masala created
del order                     # Order for Masala completed and removed
```

> Don't rely on `__del__` for critical cleanup — Python doesn't guarantee exactly when it runs. Use `with` statements and context managers for resource cleanup instead.

---

## Summary

| Concept | Detail |
|---------|--------|
| What is `__init__`? | The initialiser method — sets up an object's attributes on creation |
| When does it run? | Automatically, every time a new object is created |
| Is it mandatory? | No — but without it, objects start empty |
| Can it have defaults? | Yes — makes parameters optional |
| Can it have logic? | Yes — validation, computation, etc. |
| Return value | Must return `None` (implicitly) — never return a value from `__init__` |
| Related methods | `__new__` (creates), `__del__` (destroys) |