# Static Methods

## What is a Static Method?

A static method is a method that belongs to a class but does not depend on:
- An object (`self`)
- The class itself (`cls`)

It behaves like a regular function, but is placed inside a class because it is logically related to that class.

Static methods are defined using the `@staticmethod` decorator.

---

## Why Use Static Methods?

Use a static method when:

- The functionality is related to the class.
- It does not need to access object attributes (`self`).
- It does not need to access class attributes (`cls`).
- You want to call the method without creating an object.

Common use cases:
- Utility/helper functions
- Data formatting
- Validation
- String processing

---

## Example

```python
class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = "Water , Milk, Ginger, Honey"

cleaned = ChaiUtils.clean_ingredients(raw)

print(cleaned)
```

### Output

```python
['Water', 'Milk', 'Ginger', 'Honey']
```

---

## How It Works

### `split(",")`

Breaks the string into a list using `,` as the separator.

```python
"Water , Milk, Ginger, Honey".split(",")
```

Output:

```python
['Water ', ' Milk', ' Ginger', ' Honey']
```

---

### `strip()`

Removes extra spaces from the beginning and end of each item.

```python
" Milk".strip()
```

Output:

```python
'Milk'
```

---

### List Comprehension

```python
[item.strip() for item in text.split(",")]
```

This loops through each ingredient, removes extra spaces, and creates a new cleaned list.

---

## Notes

- Static methods can be called directly using the class name.
- No object creation is required.
- Static methods cannot access instance attributes (`self`) or class attributes (`cls`) unless they are explicitly passed as arguments.
- They are ideal for utility functions that logically belong to a class.

### Memory Trick

- **Instance Method** → Works with an object (`self`)
- **Class Method** → Works with the class (`cls`)
- **Static Method** → Works independently of both

Think of a static method as a **helper function kept inside a class for better organization**.