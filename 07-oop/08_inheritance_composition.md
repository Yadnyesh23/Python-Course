# Inheritance & Composition in Python

Both inheritance and composition are ways to **build relationships between classes** and reuse code. They answer the same question differently: *how should this class get its behaviour?*

| | Inheritance | Composition |
|---|-------------|-------------|
| Relationship | "is a" | "has a" |
| Example | A `MasalaChai` **is a** `BaseChai` | A `ChaiShop` **has a** `Chai` |
| Coupling | Tighter — child depends on parent | Looser — objects are independent |
| Flexibility | Less — changing parent affects children | More — swap components at any time |

---

## Inheritance

### What is Inheritance?

Inheritance lets a **child class** acquire all the attributes and methods of a **parent class** — and optionally add or override them. It models an "is a" relationship.

```
BaseChai  ←  MasalaChai
(parent)      (child)
```

```python
# Parent class
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

# Child class — inherits everything from BaseChai
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, clove")

masala = MasalaChai("Masala")
masala.prepare()      # inherited from BaseChai → Preparing Masala chai...
masala.add_spices()   # own method             → Adding cardamom, ginger, clove
```

### Why Do We Need Inheritance?

- **Avoid repetition** — shared logic lives in one parent class
- **Extend behaviour** — add new methods without touching the parent
- **Override behaviour** — replace a parent method with a specialised version
- **Hierarchy** — model real-world "is a" relationships naturally

### `super()` — Calling the Parent

Use `super()` to call the parent's `__init__` or any overridden method, so you don't lose the parent's setup.

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def __init__(self, type_, spice_level):
        super().__init__(type_)           # call parent's __init__ first
        self.spice_level = spice_level    # then add child-specific attribute

    def prepare(self):
        super().prepare()                 # run parent's prepare
        print(f"Spice level: {self.spice_level}")

masala = MasalaChai("Masala", "High")
masala.prepare()
```

**Output:**
```
Preparing Masala chai...
Spice level: High
```

### Types of Inheritance

```python
# Single — one parent
class MasalaChai(BaseChai):
    pass

# Multi-level — chain of parents
class SpecialMasalaChai(MasalaChai):
    pass

# Multiple — two parents
class SpicedChaiLatte(MasalaChai, LatteMixin):
    pass
```

> Python resolves multiple inheritance using the **MRO (Method Resolution Order)** — left to right, depth first. Use `ClassName.__mro__` to inspect the order.

---

## Composition

### What is Composition?

Composition means a class **contains an instance of another class** as an attribute, rather than inheriting from it. It models a "has a" relationship.

```
ChaiShop has a BaseChai
```

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class ChaiShop:
    def __init__(self):
        self.chai = BaseChai("Regular")   # ChaiShop HAS A BaseChai

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

shop = ChaiShop()
shop.serve()
```

**Output:**
```
Serving Regular chai in the shop
Preparing Regular chai...
```

### Why Do We Need Composition?

- **Loose coupling** — components can be replaced without changing the class
- **Flexibility** — mix and match different behaviours at runtime
- **Avoids deep inheritance chains** — easier to reason about
- **Easier testing** — swap real objects with mock objects

---

## Combining Inheritance and Composition

Your original example shows both working together elegantly. `ChaiShop` uses **composition** (has a chai) and `FancyChaiShop` uses **inheritance** (is a ChaiShop) — while the `chai_cls` class attribute allows the composed object to be swapped without rewriting `serve()`.

```python
# Inheritance
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, clove")

# Composition
class ChaiShop:
    chai_cls = BaseChai   # class attribute — which chai to compose with

    def __init__(self):
        self.chai = self.chai_cls("Regular")   # creates the composed object

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai   # override — now composes with MasalaChai instead

shop        = ChaiShop()
fancy_shop  = FancyChaiShop()

print("--- Regular Shop ---")
shop.serve()

print("--- Fancy Shop ---")
fancy_shop.serve()
```

**Output:**
```
--- Regular Shop ---
Serving Regular chai in the shop
Preparing Regular chai...

--- Fancy Shop ---
Serving Regular chai in the shop
Preparing Regular chai...
```

> `FancyChaiShop` overrides `chai_cls = MasalaChai` — so when `__init__` runs `self.chai_cls("Regular")`, it creates a `MasalaChai` instead of a `BaseChai`. The `serve()` method is unchanged — only the composed object is different. This pattern is called **dependency injection via class attributes**.

---

## Inheritance vs Composition — When to Use Which

**Use Inheritance when:**
- There is a genuine "is a" relationship (`MasalaChai` IS A `BaseChai`)
- You want to extend or specialise an existing class
- The child needs to be treated as the parent type (polymorphism)

**Use Composition when:**
- There is a "has a" relationship (`ChaiShop` HAS A `Chai`)
- You want to swap behaviour without changing the class
- You want to avoid tight coupling between classes

> A common principle in software design: **"favour composition over inheritance"** — composition tends to produce more flexible, maintainable code. Inheritance is powerful but overusing it creates fragile class hierarchies that are hard to change.

---

## Quick Reference

```python
# Inheritance — child gets all of parent's attributes and methods
class Child(Parent):
    def __init__(self):
        super().__init__()   # call parent constructor

# Composition — class owns an instance of another class
class Owner:
    def __init__(self):
        self.component = Component()   # has a Component

# Combined — inject which class to compose with
class Owner:
    component_cls = Component   # override in subclasses

    def __init__(self):
        self.component = self.component_cls()
```