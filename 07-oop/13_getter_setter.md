# Getter and Setter in Python

## Why do we need Getters and Setters?

Sometimes we don't want users of our class to directly access or modify attributes.

Instead of:

```python
tea.age = 10
```

we may want to:

- Validate data before updating it
- Control how data is accessed
- Hide internal implementation details
- Compute values dynamically

This is where **getters** and **setters** help.

---

## Encapsulation

Encapsulation means bundling data and methods together and controlling access to the data.

In Python, a single underscore (`_`) is used to indicate that an attribute is intended for internal use.

```python
self._age = age
```

This is a convention, not a strict restriction.

---

## Getter using `@property`

A getter allows us to control what happens when an attribute is accessed.

```python
@property
def age(self):
    return self._age + 2
```

Now:

```python
tea.age
```

actually calls:

```python
tea.age()
```

behind the scenes.

Example:

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

tea = TeaLeaf(3)

print(tea.age)
```

Output:

```python
5
```

---

## Setter using `@attribute.setter`

A setter controls what happens when a value is assigned.

```python
@age.setter
def age(self, age):
    if 1 <= age <= 5:
        self._age = age
    else:
        raise ValueError("Tea leaf must be between 1 and 5")
```

Now:

```python
tea.age = 4
```

actually calls:

```python
tea.age(4)
```

behind the scenes.

---

## Complete Example

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf must be between 1 and 5")

tea = TeaLeaf(3)

print(tea.age)

tea.age = 5

print(tea.age)
```

Output:

```python
5
7
```

---

## Why not use normal methods?

Without properties:

```python
class TeaLeaf:
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age
```

Usage:

```python
tea.get_age()
tea.set_age(4)
```

With properties:

```python
tea.age
tea.age = 4
```

Properties make the code cleaner and more Pythonic.

---

## Property Flow

```text
Reading:
tea.age
    ↓
@property getter
    ↓
returns value

Writing:
tea.age = 4
    ↓
@age.setter
    ↓
validation
    ↓
stores value
```

---

## Benefits of Getters and Setters

### Validation

```python
if age < 0:
    raise ValueError
```

### Read-only Attributes

```python
@property
def age(self):
    return self._age
```

No setter means users can read but cannot modify.

```python
tea.age = 5
```

Raises:

```python
AttributeError
```

### Computed Attributes

```python
@property
def area(self):
    return self.length * self.width
```

The value is calculated when accessed.

---

## Interview Definition

### Getter

A method used to control how an attribute is accessed.

### Setter

A method used to control and validate how an attribute is modified.

### Property

A Python feature that allows methods to be accessed like attributes using `@property`.

### Encapsulation

The practice of hiding internal data and controlling access through methods or properties.

---

## Key Points to Remember

- `@property` creates a getter.
- `@attribute.setter` creates a setter.
- `_age` means "internal use" by convention.
- Properties let methods behave like attributes.
- Getters and setters help with validation and encapsulation.
- Properties are the Pythonic replacement for traditional `get_age()` and `set_age()` methods.