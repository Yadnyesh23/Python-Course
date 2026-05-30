# Comprehensions in Python

## What are Comprehensions?

Comprehensions are a **concise, readable way to create collections** (lists, sets, dictionaries) or generate values — all in a single line, instead of writing a loop with `.append()` or manual insertion.

```python
# Without comprehension — verbose
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# With comprehension — clean
squares = [x ** 2 for x in range(1, 6)]

print(squares)   # [1, 4, 9, 16, 25]
```

---

## Why Use Comprehensions?

- **Less code** — replaces 3–4 lines with 1
- **More readable** — reads almost like plain English: *"x squared for x in range 1 to 5"*
- **Faster** — slightly more performant than equivalent `for` loops in CPython
- **Functional style** — encourages thinking in transformations and filters

---

## Where Are They Used in Real Life?

- Filtering records from a database result
- Transforming API response data into a usable format
- Building lookup dictionaries from lists
- Cleaning or normalising datasets
- Extracting unique values from a collection
- Generating test data

---

## Types of Comprehensions

Python has four types:

| Type | Syntax | Returns |
|------|--------|---------|
| List | `[expr for x in iterable]` | `list` |
| Set | `{expr for x in iterable}` | `set` |
| Dictionary | `{k: v for x in iterable}` | `dict` |
| Generator | `(expr for x in iterable)` | `generator` (lazy) |

---

