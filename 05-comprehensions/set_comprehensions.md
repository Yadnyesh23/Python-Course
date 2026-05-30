# Set Comprehensions

## What is a Set Comprehension?

A set comprehension works like a list comprehension but returns a **set** — so duplicates are automatically removed and order is not guaranteed.

```python
# List comprehension — preserves duplicates and order
squares_list = [x ** 2 for x in [1, 2, 2, 3, 3]]
print(squares_list)   # [1, 4, 4, 9, 9]

# Set comprehension — removes duplicates automatically
squares_set = {x ** 2 for x in [1, 2, 2, 3, 3]}
print(squares_set)    # {1, 4, 9}
```

---

## Syntax

```python
# Basic
{expression for item in iterable}

# With filter
{expression for item in iterable if condition}

# Nested loops
{expression for item1 in iterable1 for item2 in iterable2}
```

---

## Basic Example

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique  = {x ** 2 for x in numbers}
print(unique)   # {1, 4, 9, 16, 25}
```

```python
# Deduplicate a list of tea names
favourite_teas = [
    "Masala Tea", "Green Tea", "Masala Tea",
    "Lemon Tea", "Green Tea", "Elaichi Tea"
]

unique_teas = {tea for tea in favourite_teas}
print(unique_teas)   # {'Masala Tea', 'Green Tea', 'Lemon Tea', 'Elaichi Tea'}
```

> A simpler way to deduplicate is `set(favourite_teas)` directly — but a set comprehension lets you transform values while deduplicating.

---

## With a Filter

```python
words   = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = {word for word in words if word.startswith("a")}
print(a_words)   # {'apple', 'avocado', 'apricot'}
```

```python
# Unique even numbers only
numbers      = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_evens = {x for x in numbers if x % 2 == 0}
print(unique_evens)   # {2, 4, 6}
```

```python
# Unique words longer than 4 characters
words = ["chai", "coffee", "tea", "chai", "lemonade", "coffee"]
long  = {w for w in words if len(w) > 4}
print(long)   # {'coffee', 'lemonade'}
```

---

## Nested Loops — Flatten and Deduplicate

When working with nested data, set comprehension lets you flatten and remove duplicates in one step.

```python
recipes = {
    "Masala Chai" : ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai"  : ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
# {'ginger', 'cardamom', 'clove', 'milk', 'black pepper'}
```

> The equivalent with a list would give duplicates: `ginger` and `clove` appear in two recipes. The set comprehension automatically keeps only unique values.

---

## With Transformation

Apply a function while deduplicating:

```python
# Normalise case and deduplicate
tags = ["Python", "python", "PYTHON", "Django", "django"]
unique_tags = {tag.lower() for tag in tags}
print(unique_tags)   # {'python', 'django'}
```

```python
# Extract first letter of each unique word
words   = ["apple", "avocado", "banana", "blueberry", "cherry"]
letters = {word[0] for word in words}
print(letters)   # {'a', 'b', 'c'}
```

---

## Real-life Examples

### Extract unique domains from emails
```python
emails  = ["user@gmail.com", "admin@yahoo.com", "test@gmail.com", "dev@outlook.com"]
domains = {email.split("@")[1] for email in emails}
print(domains)   # {'gmail.com', 'yahoo.com', 'outlook.com'}
```

### Find unique file extensions in a folder
```python
files      = ["report.pdf", "notes.md", "data.csv", "summary.pdf", "code.py", "readme.md"]
extensions = {f.split(".")[-1] for f in files}
print(extensions)   # {'pdf', 'md', 'csv', 'py'}
```

### Get unique cities from a user list
```python
users        = [
    {"name": "Yadnyesh", "city": "Thane"},
    {"name": "Stavan",   "city": "Mumbai"},
    {"name": "Rohan",    "city": "Thane"},
    {"name": "Priya",    "city": "Pune"},
]
unique_cities = {user["city"] for user in users}
print(unique_cities)   # {'Thane', 'Mumbai', 'Pune'}
```

---

## Set Comprehension vs List Comprehension

| | List Comprehension | Set Comprehension |
|---|-------------------|------------------|
| Syntax | `[...]` | `{...}` |
| Duplicates | ✅ Preserved | ❌ Removed automatically |
| Order | ✅ Preserved | ❌ Not guaranteed |
| Indexing | ✅ Supported | ❌ Not supported |
| Best for | Ordered data, multiple values | Unique values, membership checks |

---

## Common Mistakes

### 1. Expecting a specific order
```python
numbers = {x for x in [3, 1, 4, 1, 5, 9, 2, 6]}
print(numbers)   # order is NOT guaranteed — e.g. {1, 2, 3, 4, 5, 6, 9}
```

### 2. Using mutable items — sets require hashable elements
```python
# ❌ Wrong — lists are not hashable
{[1, 2] for x in range(3)}   # TypeError: unhashable type: 'list'

# ✅ Right — use tuples instead
{(1, 2) for x in range(3)}
```

### 3. Confusing `{}` empty literal with set
```python
empty_set  = set()    # ✅ correct empty set
not_a_set  = {}       # ❌ this is an empty DICT, not a set
```

---

## Quick Reference

```python
# Basic deduplication
{x for x in items}

# Filter and deduplicate
{x for x in items if condition}

# Transform and deduplicate
{x.lower() for x in items}

# Flatten nested and deduplicate
{item for sublist in nested for item in sublist}

# Extract a field from a list of dicts
{d["key"] for d in list_of_dicts}
```