# Three Ways of Accessing a Base Class in Python

When a child class has its own `__init__`, it needs to also run the parent's `__init__` to set up inherited attributes. There are three ways to do this — each with different trade-offs.

---

## The Base Class

```python
class Chai:
    def __init__(self, type_, strength):
        self.type     = type_
        self.strength = strength
```

---

## Way 1 — Code Duplication ❌

Manually repeat the parent's attribute assignments inside the child.

```python
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type      = type_       # duplicated from Chai
        self.strength  = strength    # duplicated from Chai
        self.spice_level = spice_level

chai = GingerChai("Ginger", "Strong", "High")
print(chai.type)        # Ginger
print(chai.strength)    # Strong
print(chai.spice_level) # High
```

**Problems:**
- If you update `Chai.__init__` (e.g. add a new attribute), you must update every child class manually
- Violates the DRY principle (Don't Repeat Yourself)
- Easy to miss an attribute — silent bugs

> Never do this. It defeats the purpose of inheritance.

---

## Way 2 — Explicit Class Call ⚠️

Call the parent's `__init__` directly using the class name.

```python
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)   # explicit call — notice self is passed manually
        self.spice_level = spice_level

chai = GingerChai("Ginger", "Strong", "High")
print(chai.type)        # Ginger
print(chai.strength)    # Strong
print(chai.spice_level) # High
```

**How it works:** You call the method as an unbound function, so you must pass `self` explicitly.

**Problems:**
- Hardcodes the parent class name — if you rename `Chai` or change the hierarchy, every explicit call breaks
- Breaks with **multiple inheritance** — if two parents both have `__init__`, this only calls one
- More verbose than necessary

> Works for simple, single-inheritance cases but is not recommended.

---

## Way 3 — `super()` ✅

Use `super()` to call the parent's `__init__` — the right way.

```python
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)   # no 'self' — super() handles it
        self.spice_level = spice_level

chai = GingerChai("Ginger", "Strong", "High")
print(chai.type)        # Ginger
print(chai.strength)    # Strong
print(chai.spice_level) # High
```

**Why `super()` is better:**
- No hardcoded class name — refactoring is safe
- Works correctly with **multiple inheritance** — follows Python's MRO (Method Resolution Order)
- Cleaner and more readable
- The Python standard — always use this

> Notice: `super().__init__(type_, strength)` — **do not pass `self`**. `super()` already binds to the current instance. Passing `self` here is a common mistake (as shown in the original code above).

---

## The Common `super()` Mistake

```python
# ❌ Wrong — passing self explicitly to super().__init__
super().__init__(self, type_, strength)
# This passes self as the first positional argument — type_ gets the object, not the string

# ✅ Correct — super() handles self automatically
super().__init__(type_, strength)
```

---

## Comparison

| | Duplication | Explicit Call | `super()` |
|---|-------------|---------------|-----------|
| DRY | ❌ No | ✅ Yes | ✅ Yes |
| Safe to rename parent | ❌ No | ❌ No | ✅ Yes |
| Works with multiple inheritance | ❌ No | ❌ No | ✅ Yes |
| Passes `self` manually | N/A | ✅ Required | ❌ Not needed |
| Recommended | ❌ Never | ⚠️ Sometimes | ✅ Always |

---

## `super()` with Method Overriding

`super()` works for any method, not just `__init__`:

```python
class Chai:
    def prepare(self):
        print("Boiling water and milk...")

class GingerChai(Chai):
    def prepare(self):
        super().prepare()              # run parent's prepare first
        print("Adding ginger and spices")

chai = GingerChai()
chai.prepare()
```

**Output:**
```
Boiling water and milk...
Adding ginger and spices
```

---

## `super()` with Multiple Inheritance and MRO

`super()` follows Python's **MRO (Method Resolution Order)** — it doesn't always call the direct parent, it calls the next class in the MRO chain.

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

class C(A):
    def greet(self):
        super().greet()
        print("Hello from C")

class D(B, C):
    def greet(self):
        super().greet()
        print("Hello from D")

D().greet()
print(D.__mro__)
```

**Output:**
```
Hello from A
Hello from C
Hello from B
Hello from D
```

> MRO order: `D → B → C → A`. `super()` in `B` doesn't call `A` directly — it calls `C` next, because that's what the MRO says. This is why `super()` is essential for multiple inheritance to work correctly.