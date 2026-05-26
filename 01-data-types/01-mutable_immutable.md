# Data Types in Python

In Python, all data exists in the form of **objects**. Every object has three core properties:

| Property | Description | How to access |
|----------|-------------|---------------|
| **Identity** | Unique memory address | `id(obj)` |
| **Type** | What kind of object it is | `type(obj)` |
| **Value** | The actual data it holds | the object itself |

---

## Mutable vs Immutable

> **Key insight:** Mutability is about whether the *object itself* can be changed in memory — not whether a variable appears to change its value.

### The Common Misconception

It looks like numbers change when reassigned, but they don't. Here's an example:

```python
amount = 2
print("Initial amount:", amount)

amount = 12
print("Updated amount:", amount)

print(f"Id of 2  : {id(2)}")
print(f"Id of 12 : {id(12)}")
```

**Output:**
```
Initial amount: 2
Updated amount: 12
Id of 2  : 140724923220936
Id of 12 : 140724923221256
```

### What's Actually Happening

1. `amount = 2` → the integer `2` is created in memory; `amount` is a variable **pointing to** it.
2. `amount = 12` → a **new** integer `12` is created in memory; `amount` now points to `12`.
3. The original `2` is **not replaced or modified** — it still exists in memory with its own unique ID.

Because integers are **immutable**, Python never modifies the object `2`. Instead, it creates a brand new object `12` and redirects the variable. The two different IDs confirm they are entirely distinct objects.

> Think of variables as **labels**, not boxes. Reassigning a variable just moves the label — it doesn't change what's inside the old object.

---

## Immutable Data Types

Once created, these objects **cannot be modified** in memory.

| Data Type | Example | Notes |
|-----------|---------|-------|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` | Subtype of `int`; `True = 1`, `False = 0` |
| `complex` | `3 + 4j` | Real + imaginary part |
| `str` | `"hello"` | Text; supports indexing & slicing |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `frozenset` | `frozenset({1, 2, 3})` | Immutable version of a set |
| `bytes` | `b"hello"` | Immutable sequence of bytes |

---

## Mutable Data Types

These objects **can be modified** after creation — elements can be added, removed, or changed.

| Data Type | Example | Notes |
|-----------|---------|-------|
| `list` | `[1, 2, 3]` | Ordered, allows duplicates |
| `dict` | `{"key": "value"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unordered, unique elements only |
| `bytearray` | `bytearray(b"hello")` | Mutable version of `bytes` |

---

> **Quick memory trick:** Single values and `( )` → immutable. `[ ]` or `{ }` → usually mutable. The one exception is `frozenset`, which uses `{ }` syntax but is immutable.