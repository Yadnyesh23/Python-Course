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

describe("Yadnyesh", "Thane")   # ✅ correct
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

total(10, 20, 30)   # 60
total(5, 15)        # 20
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

### Single Return
```python
def square(n):
    return n ** 2

print(square(5))   # 25
```

### Multiple Return Values
Python packs multiple values into a **tuple** automatically.

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)   # 1 9
```

### Early Return
Exit a function before reaching the end — useful for guard clauses and validation.

```python
def divide(a, b):
    if b == 0:
        return "Error: division by zero"   # exit early
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Error: division by zero
```

> Early returns reduce nesting and make the "happy path" clearer.

```python
# Without early return — deeply nested
def process_order(order):
    if order is not None:
        if order["paid"]:
            if order["in_stock"]:
                print("Order confirmed")

# With early return — flat and readable
def process_order(order):
    if order is None:
        return "No order found"
    if not order["paid"]:
        return "Payment pending"
    if not order["in_stock"]:
        return "Out of stock"
    print("Order confirmed")
```

### No Return → `None`
A function with no `return` statement implicitly returns `None`.

```python
def say_hi():
    print("Hi!")

result = say_hi()
print(result)   # None
```

---

## Types of Functions

### 1. Pure Functions

A pure function **always returns the same output for the same input** and has **no side effects** — it doesn't modify anything outside itself.

```python
def add(a, b):
    return a + b

print(add(3, 4))   # always 7
```

Characteristics:
- Does not modify global variables
- Does not print, write to files, or change any external state
- Easy to test and debug

### 2. Impure Functions

An impure function **has side effects** — it modifies external state, reads input, writes to files, etc.

```python
total = 0

def add_to_total(amount):
    global total
    total += amount   # modifies external state

add_to_total(50)
add_to_total(30)
print(total)   # 80
```

| | Pure | Impure |
|---|------|--------|
| Same output for same input | ✅ Always | ❌ Not guaranteed |
| Side effects | ❌ None | ✅ Yes |
| Easy to test | ✅ Yes | ❌ Harder |
| Examples | math operations, formatting | `print()`, file I/O, DB calls |

> Prefer pure functions where possible — they are predictable, reusable, and easy to test.

---

### 3. Recursive Functions

A recursive function **calls itself** to solve a smaller version of the same problem. Every recursive function needs a **base case** to stop the recursion.

```python
def factorial(n):
    if n == 0 or n == 1:        # base case
        return 1
    return n * factorial(n - 1) # recursive call

print(factorial(5))   # 120
# 5 × 4 × 3 × 2 × 1 = 120
```

```python
# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))   # 8
```

> Without a base case, recursion runs forever and raises a `RecursionError`. Python's default recursion limit is **1000 calls**.

| | Recursion | Loop |
|---|-----------|------|
| Best for | Trees, divide & conquer | Simple repetition |
| Readability | Clean for nested problems | Cleaner for flat problems |
| Performance | Slower (call overhead) | Faster |
| Risk | Stack overflow if no base case | None |

---

### 4. Lambda Functions (Anonymous Functions)

A compact, one-line function with no name — useful for short, throwaway operations.

**Syntax:**
```python
lambda parameters: expression
```

```python
square = lambda x: x ** 2
add    = lambda a, b: a + b

print(square(5))   # 25
print(add(3, 4))   # 7
```

Lambdas are commonly used with `map()`, `filter()`, and `sorted()`:

```python
numbers = [3, 1, 5, 2, 4]

sorted_nums = sorted(numbers, key=lambda x: x)             # [1, 2, 3, 4, 5]
squared     = list(map(lambda x: x**2, numbers))           # [9, 1, 25, 4, 16]
evens       = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

| | Regular Function | Lambda |
|---|-----------------|--------|
| Name | Has a name | Anonymous |
| Lines | Multiple | Single expression only |
| Docstring | Supported | Not supported |
| Best for | Complex reusable logic | Short one-time operations |

---

## Scopes and Name Resolution (LEGB Rule)

When Python encounters a variable name, it searches for it in this order:

```
L → Local
E → Enclosing
G → Global
B → Built-in
```

This is called the **LEGB rule**. Python stops at the first scope where it finds the name.

### 1. Local Scope
Variables defined **inside a function**. Only accessible within that function.

```python
def brew():
    chai = "Masala"      # local variable
    print(chai)

brew()         # Masala
# print(chai)  # ❌ NameError — 'chai' doesn't exist outside
```

### 2. Enclosing Scope
Variables in an **outer function** accessible to an **inner nested function**.

```python
def outer():
    chai = "Elaichi"   # enclosing variable

    def inner():
        print(chai)    # reads from enclosing scope

    inner()

outer()   # Elaichi
```

### 3. Global Scope
Variables defined at the **top level** of the file — accessible anywhere.

```python
chai = "Plain"   # global variable

def brew():
    print(chai)  # can read it

brew()       # Plain
print(chai)  # Plain
```

> Reading a global is fine. To **modify** it inside a function, use the `global` keyword.

### 4. Built-in Scope
Names **built into Python** — always available without importing.

```python
print(len("Yadnyesh"))   # len  → built-in
print(type(42))           # type → built-in
print(max([3, 1, 4]))     # max  → built-in
```

---

## `nonlocal` vs `global`

### `nonlocal` — Modify an Enclosing Variable

```python
def function1():
    chai_type = "Elaichi"

    def function2():
        nonlocal chai_type     # refers to function1's variable
        chai_type = "Kesar"

    function2()
    print(chai_type)           # Kesar

function1()
```

### `global` — Modify a Global Variable

```python
chai_type = "Plain"

def function1():
    def function2():
        global chai_type       # refers to the top-level variable
        chai_type = "Irani"
    function2()

function1()
print(chai_type)               # Irani
```

### Comparison

| | `nonlocal` | `global` |
|---|-----------|---------|
| Targets | Variable in the **enclosing function** | Variable at the **module level** |
| Used in | Nested functions only | Any function |
| Affects | Only the enclosing scope | The entire module |
| Use case | Closures, stateful nested functions | Shared state across functions |

> Avoid overusing `global` — it makes code harder to trace and debug. Prefer passing values as arguments and returning results.

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

---

## Built-in Functions Reference

Python ships with many functions that are always available — no import needed.

### A
| Function | Description | Example |
|----------|-------------|---------|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `all(iterable)` | `True` if all elements are truthy | `all([1, 2, 3])` → `True` |
| `any(iterable)` | `True` if at least one element is truthy | `any([0, 0, 1])` → `True` |

### B
| Function | Description | Example |
|----------|-------------|---------|
| `bin(x)` | Binary string of an integer | `bin(10)` → `'0b1010'` |
| `bool(x)` | Converts to boolean | `bool(0)` → `False` |
| `bytearray(x)` | Creates a mutable byte array | `bytearray(3)` |
| `bytes(x)` | Creates an immutable bytes object | `bytes(3)` |

### C
| Function | Description | Example |
|----------|-------------|---------|
| `callable(obj)` | `True` if object is callable | `callable(print)` → `True` |
| `chr(i)` | Character from Unicode code point | `chr(65)` → `'A'` |

### D
| Function | Description | Example |
|----------|-------------|---------|
| `dict()` | Creates a dictionary | `dict(a=1, b=2)` |
| `dir(obj)` | Lists attributes/methods of an object | `dir([])` |
| `divmod(a, b)` | Returns `(quotient, remainder)` | `divmod(10, 3)` → `(3, 1)` |

### E
| Function | Description | Example |
|----------|-------------|---------|
| `enumerate(iterable)` | Adds index to each item | `enumerate(["a","b"])` → `(0,'a'), (1,'b')` |
| `eval(expr)` | Evaluates a string as Python code | `eval("2 + 3")` → `5` |

### F
| Function | Description | Example |
|----------|-------------|---------|
| `filter(fn, iterable)` | Filters items where `fn` returns True | `filter(lambda x: x>2, [1,2,3])` |
| `float(x)` | Converts to float | `float("3.14")` → `3.14` |
| `format(val, spec)` | Formats a value | `format(3.14, ".1f")` → `'3.1'` |
| `frozenset(x)` | Creates an immutable set | `frozenset([1, 2, 3])` |

### G
| Function | Description | Example |
|----------|-------------|---------|
| `getattr(obj, name)` | Gets attribute by name string | `getattr(obj, "age")` |
| `globals()` | Returns global symbol table as dict | `globals()` |

### H
| Function | Description | Example |
|----------|-------------|---------|
| `hasattr(obj, name)` | `True` if object has the attribute | `hasattr(obj, "name")` |
| `hash(obj)` | Returns hash value of object | `hash("hello")` |
| `help(obj)` | Prints documentation | `help(str)` |
| `hex(x)` | Hex string of an integer | `hex(255)` → `'0xff'` |

### I
| Function | Description | Example |
|----------|-------------|---------|
| `id(obj)` | Memory address (identity) of object | `id(42)` |
| `input(prompt)` | Reads user input as string | `input("Name: ")` |
| `int(x)` | Converts to integer | `int("10")` → `10` |
| `isinstance(obj, type)` | `True` if obj is instance of type | `isinstance(5, int)` → `True` |
| `iter(obj)` | Returns an iterator | `iter([1, 2, 3])` |

### L
| Function | Description | Example |
|----------|-------------|---------|
| `len(obj)` | Length of a sequence | `len("hello")` → `5` |
| `list(x)` | Converts to list | `list((1, 2, 3))` |
| `locals()` | Returns local symbol table as dict | `locals()` |

### M
| Function | Description | Example |
|----------|-------------|---------|
| `map(fn, iterable)` | Applies `fn` to each item | `map(str, [1,2,3])` |
| `max(iterable)` | Largest item | `max([3, 1, 4])` → `4` |
| `min(iterable)` | Smallest item | `min([3, 1, 4])` → `1` |

### N
| Function | Description | Example |
|----------|-------------|---------|
| `next(iterator)` | Gets next item from iterator | `next(iter([1,2,3]))` → `1` |

### O
| Function | Description | Example |
|----------|-------------|---------|
| `oct(x)` | Octal string of an integer | `oct(8)` → `'0o10'` |
| `open(file, mode)` | Opens a file | `open("file.txt", "r")` |
| `ord(char)` | Unicode code point of a character | `ord('A')` → `65` |

### P
| Function | Description | Example |
|----------|-------------|---------|
| `pow(x, y)` | `x` to the power of `y` | `pow(2, 10)` → `1024` |
| `print(*args)` | Prints to console | `print("hello")` |

### R
| Function | Description | Example |
|----------|-------------|---------|
| `range(start, stop, step)` | Generates a sequence of numbers | `range(0, 10, 2)` |
| `repr(obj)` | Printable representation of object | `repr([1,2])` → `'[1, 2]'` |
| `reversed(seq)` | Reverses a sequence | `list(reversed([1,2,3]))` |
| `round(x, n)` | Rounds to `n` decimal places | `round(3.14159, 2)` → `3.14` |

### S
| Function | Description | Example |
|----------|-------------|---------|
| `set(x)` | Creates a set | `set([1,1,2,3])` → `{1,2,3}` |
| `setattr(obj, name, val)` | Sets attribute by name string | `setattr(obj, "age", 21)` |
| `slice(start, stop)` | Creates a slice object | `slice(1, 5)` |
| `sorted(iterable)` | Returns a new sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `str(x)` | Converts to string | `str(42)` → `'42'` |
| `sum(iterable)` | Sum of all items | `sum([1,2,3])` → `6` |
| `super()` | Returns parent class object | used in class inheritance |

### T
| Function | Description | Example |
|----------|-------------|---------|
| `tuple(x)` | Converts to tuple | `tuple([1,2,3])` |
| `type(obj)` | Returns the type of an object | `type(42)` → `<class 'int'>` |

### V
| Function | Description | Example |
|----------|-------------|---------|
| `vars(obj)` | Returns `__dict__` of an object | `vars(obj)` |

### Z
| Function | Description | Example |
|----------|-------------|---------|
| `zip(*iterables)` | Pairs items from multiple iterables | `zip([1,2], ["a","b"])` → `(1,'a'), (2,'b')` |

---

## Imports, Modules and Packages

### What is a Module?

A **module** is simply a `.py` file containing Python code (functions, classes, variables) that you can reuse in other files.

```
project/
├── main.py
└── math_utils.py    ← this is a module
```

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

### Why Use Modules?

- **Reusability** — write once, import anywhere
- **Organisation** — split large codebases into logical files
- **Namespace isolation** — avoids name clashes between files

---

### Ways to Import

```python
# 1. Import the whole module — access with dot notation
import math_utils
print(math_utils.add(3, 4))

# 2. Import a specific function — use directly, no dot needed
from math_utils import add
print(add(3, 4))

# 3. Import with an alias — useful for long module names
import math_utils as mu
print(mu.add(3, 4))

# 4. Import a function with an alias
from math_utils import add as addition
print(addition(3, 4))

# 5. Import everything (avoid this — pollutes namespace)
from math_utils import *
print(add(3, 4))
```

> Prefer `import module` or `from module import specific_function` over `import *` — it keeps your namespace clean and makes the code easier to read.

---

### Standard Library Modules

Python ships with a large standard library — no installation needed.

```python
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...

import random
print(random.randint(1, 10))   # random number between 1 and 10

import os
print(os.getcwd())     # current working directory

import datetime
print(datetime.date.today())   # today's date
```

---

### What is a Package?

A **package** is a **folder** containing multiple modules, with a special file called `__init__.py` inside it.

```
project/
├── main.py
└── utils/               ← this is a package
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

```python
# Importing from a package
from utils import math_utils
from utils.math_utils import add
```

---

### What is `__init__.py`?

`__init__.py` is a special file that tells Python: **"treat this folder as a package"**.

It can be completely empty, or it can define what gets exposed when someone imports the package.

```python
# utils/__init__.py — empty file is valid
# Just its presence makes utils/ a package
```

```python
# utils/__init__.py — expose specific things at package level
from .math_utils import add
from .string_utils import capitalise
```

With this setup:
```python
# Instead of:
from utils.math_utils import add

# You can now write:
from utils import add   # cleaner!
```

---

### Module vs Package vs Library

| Term | What it is | Example |
|------|-----------|---------|
| **Module** | A single `.py` file | `math_utils.py` |
| **Package** | A folder of modules with `__init__.py` | `utils/` |
| **Library** | A collection of packages (installed via pip) | `numpy`, `pandas` |