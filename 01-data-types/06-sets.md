# Sets

## What is a Set?

A set is an **unordered collection of unique items**, denoted with `{ }`. Sets automatically eliminate duplicates and are **mutable** — but the elements inside must be immutable (e.g. strings, numbers).

```python
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" is ignored
print(fruits)  # {'apple', 'banana', 'cherry'}
```

> **Sets vs Lists:** Lists preserve order and allow duplicates. Sets do not preserve order and automatically remove duplicates.

---

## Set Operations

Sets support mathematical operations like union, intersection, and difference — making them very useful for comparing collections.

```python
essential_subs = {"DSA", "DBMS", "ML"}
optional_subs  = {"IOT", "Cyber Security", "DSA"}

all_subs       = essential_subs | optional_subs   # Union        → all unique subjects from both
common_subs    = essential_subs & optional_subs   # Intersection → subjects present in both
only_essential = essential_subs - optional_subs   # Difference   → subjects only in essential

print(f"All subjects      : {all_subs}")
print(f"Common subjects   : {common_subs}")
print(f"Only in essential : {only_essential}")
```

**Output:**
```
All subjects      : {'DSA', 'Cyber Security', 'IOT', 'DBMS', 'ML'}
Common subjects   : {'DSA'}
Only in essential : {'DBMS', 'ML'}
```

| Operator | Name | Meaning |
|----------|------|---------|
| `\|` | Union | All unique elements from both sets |
| `&` | Intersection | Only elements present in **both** sets |
| `-` | Difference | Elements in the left set but **not** in the right |

---

## Frozen Set

A **frozen set** is an **immutable** version of a set. Once created, it cannot be modified — no adding or removing elements. This makes it hashable, so it can be used as a dictionary key or stored inside another set.

```python
core_subs = frozenset({"DSA", "DBMS", "ML"})

print(core_subs)
# frozenset({'DSA', 'DBMS', 'ML'})

# core_subs.add("IOT")  # ❌ This would raise an AttributeError — frozen sets are immutable
```

| | Set | Frozen Set |
|---|-----|------------|
| Mutable | ✅ Yes | ❌ No |
| Allows duplicates | ❌ No | ❌ No |
| Ordered | ❌ No | ❌ No |
| Hashable (usable as dict key) | ❌ No | ✅ Yes |