# List Comprehensions

## What is a List Comprehension?

A list comprehension is a **concise way to create a new list** by applying an expression to each item in an iterable — all in a single line.

```python
# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(1, 6)]

print(squares)   # [1, 4, 9, 16, 25]
```

---

## Syntax

```python
# Basic
[expression for item in iterable]

# With filter
[expression for item in iterable if condition]

# With if-else transformation
[value_if_true if condition else value_if_false for item in iterable]

# Nested loops
[expression for item1 in iterable1 for item2 in iterable2]
```

---

## Basic Example

```python
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)   # [1, 4, 9, 16, 25]
```

```python
# Works on any iterable — strings too
chars = [c.upper() for c in "hello"]
print(chars)   # ['H', 'E', 'L', 'L', 'O']
```

---

## With a Filter (`if` condition)

Only include items where the condition is `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens   = [x for x in numbers if x % 2 == 0]
print(evens)   # [2, 4, 6, 8]
```

```python
# Filter strings by length
words = ["chai", "coffee", "tea", "lemonade", "milk"]
long_words = [w for w in words if len(w) > 4]
print(long_words)   # ['coffee', 'lemonade']
```

```python
# Filter out None values
data   = [1, None, 3, None, 5]
clean  = [x for x in data if x is not None]
print(clean)   # [1, 3, 5]
```

---

## With `if-else` (Transformation)

The `if-else` goes **before** the `for` when you want to transform values (not filter them).

```python
numbers = [1, 2, 3, 4, 5]
labels  = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)   # ['odd', 'even', 'odd', 'even', 'odd']
```

```python
# Replace negative numbers with 0
numbers  = [4, -1, 7, -3, 2]
positive = [x if x > 0 else 0 for x in numbers]
print(positive)   # [4, 0, 7, 0, 2]
```

> **Key rule:** `if-only` (filter) goes **after** the `for`. `if-else` (transform) goes **before** the `for`.

```python
# Filter — if AFTER for
[x for x in nums if x > 0]

# Transform — if-else BEFORE for
[x if x > 0 else 0 for x in nums]
```

---

## Nested Loops

Use multiple `for` clauses to iterate over multiple iterables.

```python
# All (row, col) pairs for a 2×3 grid
pairs = [(r, c) for r in range(2) for c in range(3)]
print(pairs)
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
```

```python
# Multiplication table (2 to 4)
table = [f"{a} × {b} = {a*b}" for a in range(2, 5) for b in range(1, 4)]
for entry in table:
    print(entry)
```

**Output:**
```
2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
3 × 1 = 3
...
```

> The order of `for` clauses in a comprehension matches the order of nested loops — outer first, inner second.

---

## Flattening a Nested List

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# Flatten and filter at the same time
matrix  = [[1, -2, 3], [-4, 5, -6]]
positives = [num for row in matrix for num in row if num > 0]
print(positives)   # [1, 3, 5]
```

---

## Nested Comprehension (2D List / Matrix)

A comprehension inside a comprehension — useful for creating grids or matrices.

```python
# 3×3 matrix of zeros
zeros = [[0 for _ in range(3)] for _ in range(3)]
print(zeros)
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
```

```python
# 3×3 identity matrix
identity = [[1 if r == c else 0 for c in range(3)] for r in range(3)]
print(identity)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
```

> Keep nested comprehensions to **2 levels max** — deeper than that, use regular loops for readability.

---

## Using `enumerate()`

When you need both the index and the value:

```python
fruits   = ["apple", "banana", "cherry"]
indexed  = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(indexed)   # ['0: apple', '1: banana', '2: cherry']
```

```python
# Find indices of items that match a condition
numbers  = [10, 25, 30, 45, 50]
indices  = [i for i, x in enumerate(numbers) if x > 30]
print(indices)   # [3, 4]
```

---

## Using `zip()`

Combine two lists element by element:

```python
names  = ["Yadnyesh", "Stavan", "Rohan"]
scores = [85, 92, 78]

report = [f"{name}: {score}" for name, score in zip(names, scores)]
print(report)   # ['Yadnyesh: 85', 'Stavan: 92', 'Rohan: 78']
```

---

## Using `range()`

```python
# Even numbers from 0 to 20
evens = [x for x in range(0, 21, 2)]
print(evens)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Squares of multiples of 3 up to 30
result = [x ** 2 for x in range(0, 31, 3)]
print(result)   # [0, 9, 36, 81, 144, 225, 324, 441, 576, 729, 900]
```

---

## Calling Functions Inside Comprehensions

```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = [double(x) for x in numbers]
print(doubled)   # [2, 4, 6, 8, 10]
```

```python
# Using built-in functions
words      = ["hello", "WORLD", "  python  "]
normalised = [w.strip().lower() for w in words]
print(normalised)   # ['hello', 'world', 'python']
```

---

## Real-life Examples

### Clean a dataset
```python
raw_names = ["  Yadnyesh", "STAVAN ", " chai "]
clean     = [name.strip().title() for name in raw_names]
print(clean)   # ['Yadnyesh', 'Stavan', 'Chai']
```

### Extract numbers from a mixed list
```python
mixed    = ["10", "hello", "25", "world", "50"]
numbers  = [int(x) for x in mixed if x.isdigit()]
print(numbers)   # [10, 25, 50]
```

### Get all files with a specific extension
```python
files = ["report.pdf", "notes.md", "data.csv", "summary.pdf", "code.py"]
pdfs  = [f for f in files if f.endswith(".pdf")]
print(pdfs)   # ['report.pdf', 'summary.pdf']
```

### Apply a discount to prices above a threshold
```python
prices      = {"chai": 20, "coffee": 80, "juice": 60, "water": 15}
discounted  = [f"{item}: ₹{round(price * 0.9)}" for item, price in prices.items() if price > 30]
print(discounted)   # ['coffee: ₹72', 'juice: ₹54']
```

---

## Common Mistakes

### 1. Using comprehension just for side effects
```python
# ❌ Wrong — comprehensions should create a new list, not just call functions
[print(x) for x in range(5)]

# ✅ Right — use a regular loop for side effects
for x in range(5):
    print(x)
```

### 2. Confusing `if-only` vs `if-else` placement
```python
# ❌ Wrong — SyntaxError
[x for x in nums if x > 0 else 0]

# ✅ Filter (if only) — after the for
[x for x in nums if x > 0]

# ✅ Transform (if-else) — before the for
[x if x > 0 else 0 for x in nums]
```

### 3. Over-complicating — hurts readability
```python
# ❌ Hard to read
result = [x ** 2 for x in range(100) if x % 2 == 0 if x % 3 == 0]

# ✅ Extract the condition into a helper
def is_valid(x):
    return x % 2 == 0 and x % 3 == 0

result = [x ** 2 for x in range(100) if is_valid(x)]
```

---

## Quick Reference

```python
# Basic transformation
[x * 2 for x in items]

# Filter only
[x for x in items if x > 0]

# Transform with condition
[x if x > 0 else 0 for x in items]

# Nested loops
[(x, y) for x in range(3) for y in range(3)]

# Flatten nested list
[item for sublist in nested for item in sublist]

# With enumerate
[f"{i}: {v}" for i, v in enumerate(items)]

# With zip
[f"{a} - {b}" for a, b in zip(list1, list2)]

# Calling a function
[fn(x) for x in items]

# Nested comprehension (2D list)
[[0 for _ in range(cols)] for _ in range(rows)]
```