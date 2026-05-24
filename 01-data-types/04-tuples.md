# Tuples

## What is a Tuple?

A tuple is an **ordered, immutable** collection of items, denoted with `( )`. It can hold any mix of data types.

```python
my_tuple = ("abc", 123, "hij", True)
```

> Since tuples are **immutable**, their values cannot be changed after creation — unlike lists.

---

## Tuple Packing & Unpacking

Python lets you assign multiple variables in a single line:

```python
yadnyesh, stavan = 23, 24
```

This works because `23, 24` is implicitly a tuple `(23, 24)`, and Python **unpacks** it into the two variables. This is called **tuple unpacking**.

---

## Swapping Variables

Normally swapping two values requires a third temporary variable. In Python, tuple unpacking makes it a one-liner:

```python
yadnyesh, stavan = 23, 24
print(f"Before swap — Yadnyesh: {yadnyesh}, Stavan: {stavan}")

yadnyesh, stavan = stavan, yadnyesh
print(f"After swap  — Yadnyesh: {yadnyesh}, Stavan: {stavan}")
```

**Output:**
```
Before swap — Yadnyesh: 23, Stavan: 24
After swap  — Yadnyesh: 24, Stavan: 23
```

> Python evaluates the right-hand side `stavan, yadnyesh` as a tuple first, then unpacks it — so no third variable is needed.

---

## Membership Testing

Use the `in` operator to check if a value exists in a tuple:

```python
cities = ("Thane", "Mumbai", "Pune")

print(f"Is Delhi available? : {'Delhi' in cities}")
print(f"Is Mumbai available?: {'Mumbai' in cities}")
```

**Output:**
```
Is Delhi available? : False
Is Mumbai available?: True
```

> `in` returns `True` or `False` and works on any sequence — tuples, lists, strings, etc.