# Data Types in Python

In Python, all data exists in the form of **objects**. Every object has three core properties:

- **Identity** — a unique ID (memory address), returned by `id()`
- **Type** — what kind of object it is (int, str, list, etc.)
- **Value** — the actual data it holds

---

## Mutable vs Immutable

> **Key insight:** Mutability is about whether the *object itself* can be changed in memory — not whether a variable's value appears to change.

### The Common Misconception

It looks like numbers change, but they don't. Here's an example:

```python
amount = 2
print("Initial amount:", amount)

amount = 12
print("Updated amount:", amount)

print(f"Id of 2  : {id(2)}")
print(f"Id of 12 : {id(12)}")
\```

**Output:**
\```
Initial amount: 2
Updated amount: 12
Id of 2  : 140724923220936
Id of 12 : 140724923221256
\```

### What's Actually Happening

1. `amount = 2` → the integer `2` is created in memory; `amount` is a *variable* pointing to it.
2. `amount = 12` → a *new* integer `12` is created in memory; `amount` now points to `12`.
3. The original `2` is **not replaced or modified** — it still exists in memory with its own unique ID.

Because integers are **immutable**, Python never modifies the object `2`. Instead, it creates a brand new object `12` and redirects the variable. The two IDs confirm they are distinct objects.

> Think of variables as **labels**, not boxes. Reassigning a variable just moves the label — it doesn't change what's inside the old object.
```

Copy that and save it as a `.md` file. The backslashes before the closing triple-backticks (`\`\`\``) are just escape characters for display here — in your actual file they should be plain ` ``` `.

Would you like me to create it as a downloadable `.md` file instead?