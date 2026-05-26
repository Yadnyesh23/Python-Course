# Dictionaries in Python

A dictionary is an **ordered, mutable** collection of **key-value pairs**, denoted with `{ }`.

```python
student = {
    "name": "Yadnyesh",
    "age": 21,
    "city": "Thane"
}
```

> Since Python 3.7+, dictionaries maintain **insertion order** — the order you add items is the order they stay.

---

## Key Rules

- Keys must be **unique** — duplicate keys overwrite the previous value
- Keys must be **immutable** — strings, numbers, and tuples are valid keys; lists and sets are not
- Values can be **anything** — strings, numbers, lists, other dicts, etc.

```python
# Valid keys
d = {
    "name": "Yadnyesh",   # string key ✅
    42: "answer",          # integer key ✅
    (1, 2): "coords"       # tuple key ✅
}

# Invalid key
# {[1, 2]: "value"}  ❌ → TypeError: unhashable type: 'list'
```

---

## Creating a Dictionary

```python
# Method 1: literal syntax
person = {"name": "Yadnyesh", "age": 21}

# Method 2: dict() constructor
person = dict(name="Yadnyesh", age=21)

# Method 3: empty dict, then add
person = {}
person["name"] = "Yadnyesh"
person["age"]  = 21

# Method 4: fromkeys() — create with default value
keys    = ["name", "age", "city"]
default = dict.fromkeys(keys, "unknown")
print(default)  # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
```

---

## Accessing Values

```python
student = {"name": "Yadnyesh", "age": 21, "city": "Thane"}

# Method 1: square bracket notation
print(student["name"])      # Yadnyesh
# print(student["grade"])   # ❌ KeyError if key doesn't exist

# Method 2: .get() — safe access, returns None if key missing
print(student.get("age"))          # 21
print(student.get("grade"))        # None
print(student.get("grade", "N/A")) # N/A  ← custom default value
```

> Always prefer `.get()` over `[ ]` when the key might not exist — it avoids a `KeyError` crash.

---

## Modifying a Dictionary

```python
student = {"name": "Yadnyesh", "age": 21}

# Add a new key
student["city"] = "Thane"

# Update an existing key
student["age"] = 22

# Update multiple keys at once
student.update({"age": 23, "city": "Mumbai"})

print(student)  # {'name': 'Yadnyesh', 'age': 23, 'city': 'Mumbai'}
```

---

## Removing Items

```python
student = {"name": "Yadnyesh", "age": 21, "city": "Thane", "grade": "A"}

# pop() — removes by key and returns the value
removed = student.pop("grade")
print(removed)   # A

# popitem() — removes and returns the LAST inserted key-value pair
last = student.popitem()
print(last)      # ('city', 'Thane')

# del — removes by key, no return value
del student["age"]

# clear() — empties the entire dictionary
student.clear()
print(student)   # {}
```

---

## Looping Through a Dictionary

```python
student = {"name": "Yadnyesh", "age": 21, "city": "Thane"}

# Loop over keys (default)
for key in student:
    print(key)

# Loop over values
for value in student.values():
    print(value)

# Loop over key-value pairs
for key, value in student.items():
    print(f"{key} : {value}")
```

**Output of `.items()` loop:**
```
name : Yadnyesh
age  : 21
city : Thane
```

---

## Useful Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.get(key, default)` | Safe value access | `d.get("age", 0)` |
| `.keys()` | Returns all keys | `d.keys()` |
| `.values()` | Returns all values | `d.values()` |
| `.items()` | Returns all key-value pairs | `d.items()` |
| `.update(dict)` | Merges another dict in | `d.update({"x": 1})` |
| `.pop(key)` | Removes key, returns value | `d.pop("age")` |
| `.popitem()` | Removes last inserted pair | `d.popitem()` |
| `.clear()` | Removes all items | `d.clear()` |
| `.copy()` | Returns a shallow copy | `d2 = d.copy()` |
| `dict.fromkeys(keys, val)` | Creates dict with default values | `dict.fromkeys(["a","b"], 0)` |

---

## Membership Testing

The `in` operator checks for **keys**, not values:

```python
student = {"name": "Yadnyesh", "age": 21}

print("name" in student)         # True
print("city" in student)         # False
print(21 in student.values())    # True  ← check values explicitly
```

---

## Nested Dictionaries

Dictionaries can contain other dictionaries as values:

```python
students = {
    "student1": {"name": "Yadnyesh", "age": 21},
    "student2": {"name": "Stavan",   "age": 22},
}

print(students["student1"]["name"])  # Yadnyesh
print(students["student2"]["age"])   # 22
```

---

## Dictionary Comprehension

A concise way to create dictionaries in one line:

```python
# Squares of numbers 1–5
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter only even numbers
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}
```

---

## Merging Dictionaries

```python
defaults = {"theme": "light", "language": "en"}
user_prefs = {"theme": "dark"}

# Method 1: update() — modifies in place
defaults.update(user_prefs)

# Method 2: | operator (Python 3.9+) — creates a new dict
merged = defaults | user_prefs
print(merged)  # {'theme': 'dark', 'language': 'en'}
```

> If both dicts have the same key, the **right-hand dict's value wins**.

---

## Shallow vs Deep Copy

```python
import copy

original = {"name": "Yadnyesh", "scores": [90, 85, 92]}

shallow = original.copy()         # top-level copy; nested objects still shared
deep    = copy.deepcopy(original) # fully independent copy at all levels

shallow["scores"].append(100)
print(original["scores"])  # [90, 85, 92, 100] ← affected by shallow copy!
print(deep["scores"])      # [90, 85, 92]       ← deep copy is unaffected
```

> Use `copy.deepcopy()` when your dictionary contains nested mutable objects like lists or other dicts.