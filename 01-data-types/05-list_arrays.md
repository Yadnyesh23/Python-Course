# Lists

## What is a List?

A list is an **ordered, mutable** collection of items, denoted with `[ ]`. Unlike tuples, lists can be modified after creation — you can add, remove, or change elements.

```python
fruits = ["apple", "banana", "cherry"]
```

> Lists can hold any mix of data types — integers, strings, other lists, etc.

---

## Common List Operations

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Adds `x` to the **end** of the list | `fruits.append("mango")` |
| `insert(i, x)` | Inserts `x` at a **specific index** `i` | `fruits.insert(1, "mango")` |
| `remove(x)` | Removes the **first occurrence** of value `x` | `fruits.remove("banana")` |
| `pop(i)` | Removes and **returns** the item at index `i` (default: last) | `fruits.pop()` |
| `extend(lst)` | Appends **all items** from another list | `fruits.extend(["kiwi", "grape"])` |
| `reverse()` | Reverses the list **in place** | `fruits.reverse()` |
| `sort()` | Sorts the list **in place** | `fruits.sort()` |
| `max(lst)` | Returns the **largest** item | `max(fruits)` |
| `min(lst)` | Returns the **smallest** item | `min(fruits)` |

### append vs insert

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")       # Always adds to the END
# ["apple", "banana", "cherry", "mango"]

fruits.insert(1, "kiwi")     # Adds at index 1, shifting others right
# ["apple", "kiwi", "banana", "cherry", "mango"]
```

> Use `append` when you don't care about position. Use `insert` when you need to place an item at a specific index.

### pop vs remove

```python
fruits = ["apple", "banana", "cherry"]

fruits.pop()            # Removes and returns the LAST item → "cherry"
fruits.pop(0)           # Removes and returns item at index 0 → "apple"

fruits.remove("banana") # Removes the FIRST occurrence of the VALUE "banana"
```

> Use `pop` when you know the **index** (or want the last item). Use `remove` when you know the **value**.

---

## Operator Overloading

Python's `+` and `*` operators work on lists too, with intuitive behaviour:

```python
list1 = ["abc", "efg"]
list2 = ["pqr", "xyz"]

list3 = list1 + list2   # Concatenation → combines both lists
list4 = list1 * 3       # Repetition   → repeats list1 three times

print(list3)  # ['abc', 'efg', 'pqr', 'xyz']
print(list4)  # ['abc', 'efg', 'abc', 'efg', 'abc', 'efg']
```

**Output:**
```
['abc', 'efg', 'pqr', 'xyz']
['abc', 'efg', 'abc', 'efg', 'abc', 'efg']
```

> This is called **operator overloading** — the same `+` and `*` symbols behave differently depending on the data type they operate on (numbers vs lists vs strings).