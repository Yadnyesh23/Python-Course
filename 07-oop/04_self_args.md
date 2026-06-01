# The `self` Argument in Python

## What is `self`?

`self` is the first parameter of every instance method in a class. It is a reference to the **specific object** that called the method — giving the method access to that object's attributes and other methods.

```python
class Chai:
    def __init__(self, name):
        self.name = name   # 'self' binds 'name' to THIS specific object

masala = Chai("Masala Chai")
ginger = Chai("Ginger Chai")

print(masala.name)   # Masala Chai  ← masala's own
print(ginger.name)   # Ginger Chai  ← ginger's own
```

> `self` is what separates one object's data from another's. Without it, all instances would share the same variables.

---

## Why Do We Need `self`?

When you call `cup.describe()`, Python needs to know *which* cup you're describing. `self` carries that information — it is automatically set to the object that made the call.

Without `self`, a method has no way to reach the object's own data:

```python
# Without self — can't access instance data
class Chai:
    def describe():         # no self — broken
        return "A chai"     # which chai? unknown

# With self — knows exactly which object
class Chai:
    def describe(self):
        return f"A chai named {self.name}"   # reaches THIS object's name
```

---

## How `self` Works Under the Hood

When you write `cup.describe()`, Python silently translates it to `Chaicup.describe(cup)` — passing the object in as the first argument automatically. These two calls are identical:

```python
class Chaicup:
    size = 150   # ml

    def describe(self):
        return f"A {self.size}ml Chai cup"

cup = Chaicup()

# Method 1 — normal call (Python passes self automatically)
print(cup.describe())

# Method 2 — calling via the class directly (self passed manually)
print(Chaicup.describe(cup))   # identical result
```

**Output:**
```
A 150ml Chai cup
A 150ml Chai cup
```

> `cup.describe()` is just shorthand. Python automatically fills in `self = cup` behind the scenes. Calling `Chaicup.describe()` with no argument would raise a `TypeError` because `self` is missing.

---

## `self` Keeps Each Object's Data Separate

Every object gets its own namespace. `self` is what ties a method to the correct one.

```python
class Chaicup:
    size = 150   # ml

    def describe(self):
        return f"A {self.size}ml Chai cup"

cup     = Chaicup()
cup_two = Chaicup()

print(cup.describe())       # A 150ml Chai cup
print(cup_two.describe())   # A 150ml Chai cup

# Give cup its own size — shadows the class attribute
cup.size = 200
print(cup.describe())       # A 200ml Chai cup  ← cup's own
print(cup_two.describe())   # A 150ml Chai cup  ← cup_two still reads from class
```

> `self.size` inside `describe()` resolves to `cup.size` for `cup` and `cup_two.size` for `cup_two`. Same method, different objects, different results.

---

## `self` is Just a Convention

Python does not enforce the name `self` — you can use any name. But `self` is the universal standard and you should always use it.

```python
class Chai:
    def describe(this):         # valid but non-standard ⚠️
        return f"Chai: {this.name}"

class Chai:
    def describe(self):         # ✅ always use this
        return f"Chai: {self.name}"
```

---

## What You Can Do with `self`

```python
class Chai:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def describe(self):
        return f"{self.name} costs ₹{self.price}"   # access attributes

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)            # modify attributes
        return self                                  # return self for chaining

    def reset(self):
        self.price = 0
        self.apply_discount(0)                       # call another method via self

masala = Chai("Masala Chai", 40)
print(masala.describe())          # Masala Chai costs ₹40
masala.apply_discount(10)
print(masala.describe())          # Masala Chai costs ₹36.0
```

---

## Summary

| Question | Answer |
|----------|--------|
| What is `self`? | A reference to the current object instance |
| Where does it come from? | Python passes it automatically when you call `obj.method()` |
| Why do we need it? | So methods know which object's data to use |
| Is the name mandatory? | No, but `self` is the universal convention |
| What can you do with it? | Read attributes, modify attributes, call other methods |