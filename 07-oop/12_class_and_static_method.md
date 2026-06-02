# Class Method vs Static Method

## What is the Difference Between Them?

Both `@classmethod` and `@staticmethod` are methods that belong to a class, but they serve different purposes.

| Feature | Class Method | Static Method |
|----------|-------------|-------------|
| Decorator | `@classmethod` | `@staticmethod` |
| First Parameter | `cls` | None |
| Access Class Attributes | ✅ Yes | ❌ No |
| Access Instance Attributes | ❌ No | ❌ No |
| Can Create Objects | ✅ Yes | ❌ Usually No |
| Common Use | Alternative constructors | Utility/helper functions |

---

## What Do They Do?

### Class Method

A class method receives the class itself as the first argument (`cls`).

```python
@classmethod
def my_method(cls):
    pass
```

It can:
- Access class variables
- Modify class variables
- Create and return objects of the class

---

### Static Method

A static method receives no special first argument.

```python
@staticmethod
def my_method():
    pass
```

It:
- Cannot access `self`
- Cannot access `cls`
- Works like a normal function that is grouped inside a class

---

## What Is Their Purpose?

### Purpose of Class Methods

Class methods are commonly used as **alternative constructors**.

For example, instead of creating an object directly:

```python
order = ChaiOrder("Masala", "Medium", "Large")
```

you can create it from different formats:

```python
order = ChaiOrder.from_dict(data)
order = ChaiOrder.from_string(text)
```

This makes object creation more flexible.

---

### Purpose of Static Methods

Static methods are used for helper functions that are related to a class but do not need object data or class data.

Examples:
- Validation
- String cleaning
- Unit conversion
- Utility functions

---

## Example: Class Method

```python
class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


order = ChaiOrder.from_string("Masala-Medium-Large")

print(order.tea_type)
```

### Output

```python
Masala
```

### Note

The class method uses `cls(...)` to create and return a new object.

---

## Example: Static Method

```python
class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


ingredients = ChaiUtils.clean_ingredients(
    "Water , Milk, Ginger, Honey"
)

print(ingredients)
```

### Output

```python
['Water', 'Milk', 'Ginger', 'Honey']
```

### Note

The static method does not create objects and does not use class data. It simply performs a utility task.

---

## Key Notes

### Class Method

- Receives `cls`
- Works with class-level data
- Often used as an alternative constructor
- Can create and return objects

### Static Method

- Receives no special argument
- Cannot access class or instance data directly
- Used for utility/helper functions
- Does not depend on object state

---

## Memory Trick

### Instance Method

```python
def method(self):
```

Works with an object.

---

### Class Method

```python
@classmethod
def method(cls):
```

Works with the class.

---

### Static Method

```python
@staticmethod
def method():
```

Works independently of both.

---

## Quick Summary

- **Instance Method** → Uses object data (`self`)
- **Class Method** → Uses class data (`cls`)
- **Static Method** → Uses neither; acts as a utility function

A common interview answer:

> A class method works with the class itself and is often used as an alternative constructor, whereas a static method does not depend on either the class or its objects and is mainly used for utility functions.