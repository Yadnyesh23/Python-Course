# Dictionary Comprehensions

## What is a Dictionary Comprehension?

A dictionary comprehension is a concise way to **create or transform a dictionary** in a single line, instead of building it with a loop and manual key assignment.

```python
# Traditional loop
squares = {}
for x in range(1, 6):
    squares[x] = x ** 2

# Dictionary comprehension — same result, one line
squares = {x: x ** 2 for x in range(1, 6)}

print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Syntax

```python
# Basic
{key_expr: value_expr for item in iterable}

# With filter
{key_expr: value_expr for item in iterable if condition}

# From an existing dictionary
{key_expr: value_expr for key, value in dict.items()}

# Nested loops
{key_expr: value_expr for item1 in iterable1 for item2 in iterable2}
```

---

## Basic Example

```python
numbers = [1, 2, 3, 4, 5]
squares = {x: x ** 2 for x in numbers}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Cube of numbers
cubes = {x: x ** 3 for x in range(1, 6)}
print(cubes)   # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

```python
# Map characters to their ASCII values
chars = {c: ord(c) for c in "hello"}
print(chars)   # {'h': 104, 'e': 101, 'l': 108, 'o': 111}
```

---

## Transforming an Existing Dictionary

Apply an operation to every value in a dictionary.

```python
# Currency conversion — INR to USD
chai_prices_inr = {
    "Masala Chai": 40,
    "Green Tea"  : 60,
    "Lemon Tea"  : 200,
}

chai_prices_usd = {tea: round(price / 80, 2) for tea, price in chai_prices_inr.items()}

print(f"Prices in INR : {chai_prices_inr}")
print(f"Prices in USD : {chai_prices_usd}")
```

**Output:**
```
Prices in INR : {'Masala Chai': 40, 'Green Tea': 60, 'Lemon Tea': 200}
Prices in USD : {'Masala Chai': 0.5, 'Green Tea': 0.75, 'Lemon Tea': 2.5}
```

```python
# Apply 10% discount to all items
prices     = {"chai": 20, "coffee": 80, "juice": 60}
discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
print(discounted)   # {'chai': 18.0, 'coffee': 72.0, 'juice': 54.0}
```

```python
# Normalise all keys to lowercase
raw = {"Name": "Yadnyesh", "CITY": "Thane", "Age": 21}
normalised = {k.lower(): v for k, v in raw.items()}
print(normalised)   # {'name': 'Yadnyesh', 'city': 'Thane', 'age': 21}
```

---

## Swapping Keys and Values

```python
original = {"a": 1, "b": 2, "c": 3}
swapped  = {v: k for k, v in original.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}
```

> This only works reliably when values are **unique and hashable**. If two keys share the same value, one will be overwritten.

```python
# ⚠️ Duplicate values — one entry lost
original = {"a": 1, "b": 1, "c": 2}
swapped  = {v: k for k, v in original.items()}
print(swapped)   # {1: 'b', 2: 'c'}  ← 'a' is overwritten by 'b'
```

---

## With a Filter

### Filter by value
```python
scores = {"Yadnyesh": 85, "Stavan": 42, "Rohan": 91, "Priya": 38}
passed = {name: score for name, score in scores.items() if score >= 50}
print(passed)   # {'Yadnyesh': 85, 'Rohan': 91}
```

### Filter by key
```python
data    = {"name": "Yadnyesh", "age": 21, "password": "secret", "city": "Thane"}
public  = {k: v for k, v in data.items() if k != "password"}
print(public)   # {'name': 'Yadnyesh', 'age': 21, 'city': 'Thane'}
```

### Filter out None values
```python
raw     = {"name": "Yadnyesh", "age": None, "city": "Thane", "phone": None}
clean   = {k: v for k, v in raw.items() if v is not None}
print(clean)   # {'name': 'Yadnyesh', 'city': 'Thane'}
```

---

## Building from Two Lists Using `zip()`

```python
keys   = ["name", "age", "city"]
values = ["Yadnyesh", 21, "Thane"]

person = {k: v for k, v in zip(keys, values)}
print(person)   # {'name': 'Yadnyesh', 'age': 21, 'city': 'Thane'}
```

```python
# Subject → grade mapping
subjects = ["DSA", "DBMS", "ML", "OS"]
grades   = ["A", "B+", "A+", "B"]

report = {sub: grade for sub, grade in zip(subjects, grades)}
print(report)   # {'DSA': 'A', 'DBMS': 'B+', 'ML': 'A+', 'OS': 'B'}
```

---

## Default Values with `fromkeys()`

Create a dictionary with all keys set to the same default value:

```python
keys    = ["name", "age", "city"]
default = dict.fromkeys(keys, "unknown")
print(default)   # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
```

Or use a comprehension for more control:

```python
subjects  = ["DSA", "DBMS", "ML"]
gradebook = {sub: [] for sub in subjects}   # each subject gets its own empty list
print(gradebook)   # {'DSA': [], 'DBMS': [], 'ML': []}
```

> Don't use `dict.fromkeys(keys, [])` for mutable defaults — all keys will share the **same** list object. Use a comprehension instead.

---

## Nested Dictionary Comprehension

```python
# Build a multiplication table as a nested dict
table = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}
print(table)
# {1: {1: 1, 2: 2, 3: 3},
#  2: {1: 2, 2: 4, 3: 6},
#  3: {1: 3, 2: 6, 3: 9}}

print(table[2][3])   # 6
```

> Keep nested comprehensions to **2 levels max** — deeper than that, use regular loops.

---

## Real-life Examples

### Word frequency counter
```python
sentence = "chai is great and chai is healthy"
words    = sentence.split()
freq     = {word: words.count(word) for word in set(words)}
print(freq)   # {'great': 1, 'chai': 2, 'and': 1, 'is': 2, 'healthy': 1}
```

### Categorise students by pass/fail
```python
scores    = {"Yadnyesh": 85, "Stavan": 42, "Rohan": 91, "Priya": 38}
result    = {name: ("Pass" if score >= 50 else "Fail") for name, score in scores.items()}
print(result)   # {'Yadnyesh': 'Pass', 'Stavan': 'Fail', 'Rohan': 'Pass', 'Priya': 'Fail'}
```

### Index a list of dicts by a key field
```python
users = [
    {"id": 1, "name": "Yadnyesh"},
    {"id": 2, "name": "Stavan"},
    {"id": 3, "name": "Rohan"},
]
by_id = {user["id"]: user["name"] for user in users}
print(by_id)   # {1: 'Yadnyesh', 2: 'Stavan', 3: 'Rohan'}
```

---

## Common Mistakes

### 1. Forgetting `.items()` when iterating a dict
```python
scores = {"Yadnyesh": 85, "Stavan": 42}

# ❌ Wrong — iterates only over keys
{k: v for k, v in scores}       # ValueError

# ✅ Correct
{k: v for k, v in scores.items()}
```

### 2. Assuming swapped keys are always unique
```python
# ❌ Silent data loss if values aren't unique
{v: k for k, v in {"a": 1, "b": 1}.items()}   # {1: 'b'} — 'a' lost
```

### 3. Using `fromkeys()` with a mutable default
```python
# ❌ All keys share the SAME list — modifying one affects all
bad = dict.fromkeys(["x", "y", "z"], [])
bad["x"].append(1)
print(bad)   # {'x': [1], 'y': [1], 'z': [1]} ← unexpected!

# ✅ Use comprehension — each key gets its own list
good = {k: [] for k in ["x", "y", "z"]}
good["x"].append(1)
print(good)   # {'x': [1], 'y': [], 'z': []} ← correct
```

---

## Quick Reference

```python
# Basic
{x: x**2 for x in items}

# From existing dict
{k: v * 2 for k, v in d.items()}

# Filter by value
{k: v for k, v in d.items() if v > 0}

# Filter by key
{k: v for k, v in d.items() if k != "password"}

# Swap keys and values
{v: k for k, v in d.items()}

# From two lists
{k: v for k, v in zip(keys, values)}

# Conditional value
{k: "Pass" if v >= 50 else "Fail" for k, v in scores.items()}

# Normalise keys
{k.lower(): v for k, v in d.items()}

# Remove None values
{k: v for k, v in d.items() if v is not None}
```