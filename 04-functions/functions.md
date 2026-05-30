# Functions in Python

## What is a Function?

A function is a **reusable block of code** that performs a specific task. You define it once and can call it as many times as needed.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Yadnyesh")   # Hello, Yadnyesh!
greet("Stavan")     # Hello, Stavan!
```

---

## Why Do We Need Functions?

- **Avoid repetition** — write logic once, reuse anywhere (DRY: Don't Repeat Yourself)
- **Readability** — break a large program into small, named, understandable pieces
- **Maintainability** — fix a bug in one place instead of everywhere
- **Testability** — test small units of logic independently

---

## Defining and Calling Functions

**Syntax:**
```python
def function_name(parameters):
    # body
    return value   # optional
```

```python
# No parameters, no return
def say_hello():
    print("Hello!")

# With parameters
def add(a, b):
    print(a + b)

# With return value
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)   # 20
```

---

## Types of Arguments

### 1. Positional Arguments
Passed in order — position matters.

```python
def describe(name, city):
    print(f"{name} is from {city}")

describe("Yadnyesh", "Thane")   # ✅
describe("Thane", "Yadnyesh")   # ⚠️ wrong meaning, no error
```

### 2. Keyword Arguments
Passed by name — order doesn't matter.

```python
describe(city="Thane", name="Yadnyesh")   # ✅ same result
```

### 3. Default Arguments
Used when no value is passed for that parameter.

```python
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("Yadnyesh")               # Good morning, Yadnyesh!
greet("Stavan", "Good night")   # Good night, Stavan!
```

> Default parameters must always come **after** non-default ones.

### 4. `*args` — Variable Positional Arguments
Accept any number of positional arguments as a **tuple**.

```python
def total(*prices):
    print(sum(prices))

total(10, 20, 30)       # 60
total(5, 15)            # 20
```

### 5. `**kwargs` — Variable Keyword Arguments
Accept any number of keyword arguments as a **dictionary**.

```python
def show_details(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

show_details(name="Yadnyesh", city="Thane", age=21)
```

**Output:**
```
name : Yadnyesh
city : Thane
age  : 21
```

---

## Return Values

A function can return a single value, multiple values, or nothing.

```python
# Single return
def square(n):
    return n ** 2

# Multiple return values (returned as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)   # 1 9

# No return → returns None implicitly
def say_hi():
    print("Hi!")

result = say_hi()
print(result)   # None
```

---

## Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| Reusability — write once, use many times | Overhead for very small, one-time tasks |
| Cleaner, readable code | Poorly named functions reduce clarity |
| Easier debugging and testing | Overusing parameters can get complex |
| Encourages modular design | Scope issues if globals are overused |

---

## Scopes and Name Resolution (LEGB Rule)

When Python encounters a variable name, it searches for it in this order:

```
L → Local
E → Enclosing
G → Global
B → Built-in
```

This is called the **LEGB rule**.

---

### 1. Local Scope

Variables defined **inside a function**. Only accessible within that function.

```python
def brew():
    chai = "Masala"      # local variable
    print(chai)

brew()         # Masala
# print(chai)  # ❌ NameError — 'chai' doesn't exist outside
```

---

### 2. Enclosing Scope

Variables in an **outer function** that are accessible to an **inner (nested) function**.

```python
def outer():
    chai = "Elaichi"        # enclosing variable

    def inner():
        print(chai)         # can access outer's variable

    inner()

outer()   # Elaichi
```

---

### 3. Global Scope

Variables defined at the **top level** of a script — accessible anywhere in the file.

```python
chai = "Plain"   # global variable

def brew():
    print(chai)   # can read global variable

brew()      # Plain
print(chai) # Plain
```

> Reading a global variable inside a function is fine. But to **modify** it, you must use the `global` keyword.

---

### 4. Built-in Scope

Names that are **built into Python** — always available without importing.

```python
print(len("Yadnyesh"))   # len is a built-in function
print(type(42))           # type is a built-in function
print(range(5))           # range is a built-in function
```

Common built-ins: `print`, `len`, `type`, `range`, `int`, `str`, `list`, `dict`, `max`, `min`, `sum`, `input`, `open`

---

## `nonlocal` vs `global`

### `nonlocal` — Modify an Enclosing Variable

Used inside a **nested function** to modify a variable from the **outer function**.

```python
def function1():
    chai_type = "Elaichi"

    def function2():
        nonlocal chai_type        # refers to function1's chai_type
        chai_type = "Kesar"

    function2()
    print(chai_type)              # Kesar

function1()
```

**Output:**
```
Kesar
```

---

### `global` — Modify a Global Variable

Used inside **any function** to modify a variable defined at the **top (global) level**.

```python
chai_type = "Plain"

def function1():
    def function2():
        global chai_type          # refers to the top-level chai_type
        chai_type = "Irani"

    function2()

function1()
print(chai_type)                  # Irani
```

**Output:**
```
Irani
```

---

### nonlocal vs global — Quick Comparison

| | `nonlocal` | `global` |
|---|-----------|---------|
| Targets | Variable in the **enclosing function** | Variable at the **module/top level** |
| Used in | Nested functions only | Any function |
| Affects | Only the enclosing scope | The entire module |
| Use case | Closures, stateful nested functions | Shared state across functions |

> Avoid overusing `global` — it makes code harder to debug. Prefer passing values as arguments and returning results instead.

---

## Lambda Functions (Anonymous Functions)

A compact, one-line function with no name — useful for short operations.

**Syntax:**
```python
lambda parameters: expression
```

```python
square  = lambda x: x ** 2
add     = lambda a, b: a + b

print(square(5))    # 25
print(add(3, 4))    # 7
```

Lambdas are commonly used with `map()`, `filter()`, and `sorted()`:

```python
numbers = [3, 1, 5, 2, 4]

sorted_nums   = sorted(numbers, key=lambda x: x)           # [1, 2, 3, 4, 5]
squared       = list(map(lambda x: x**2, numbers))         # [9, 1, 25, 4, 16]
evens         = list(filter(lambda x: x % 2 == 0, numbers))# [2, 4]
```

---

## Docstrings

Document your functions using a docstring — the first string inside the function body.

```python
def add(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b

print(add.__doc__)   # prints the docstring
help(add)            # formatted output in terminal
```