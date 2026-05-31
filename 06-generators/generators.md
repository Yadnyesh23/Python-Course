# Generators in Python

## What is a Generator?

A generator is a special type of function that **produces values one at a time, on demand** — instead of computing and returning everything at once. It uses the `yield` keyword instead of `return`.

```python
# Regular function — computes and returns all values at once
def get_squares(n):
    result = []
    for x in range(n):
        result.append(x ** 2)
    return result

# Generator function — produces one value at a time
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
```

---

## Why Use Generators?

### 1. Save Memory
A regular function builds the entire result in memory. A generator produces values one by one — only the current value is held in memory at any time.

```python
import sys

# List — all 1 million numbers stored in memory
numbers_list = [x for x in range(1_000_000)]
print(sys.getsizeof(numbers_list))   # ~8 MB

# Generator — only stores the current state
numbers_gen = (x for x in range(1_000_000))
print(sys.getsizeof(numbers_gen))    # ~112 bytes
```

### 2. Lazy Evaluation
Values are computed **only when requested** — not upfront. This is useful when you don't know how many values you'll actually need.

### 3. Work with Infinite Sequences
Generators can produce values forever — something impossible with a list.

---

## Generator Keywords and Methods

Python gives you five tools to work with generators:

| Tool | Purpose |
|------|---------|
| `yield` | Pause the function and produce a value |
| `next()` | Resume the generator and get the next value |
| `send()` | Resume the generator and pass a value in |
| `yield from` | Delegate to another generator or iterable |
| `.close()` | Stop the generator early |

---

## `yield`

`yield` is what makes a function a generator. It pauses the function, sends a value out, and saves the entire execution state (local variables, position) until the next call.

### `yield` vs `return`

| | `return` | `yield` |
|---|----------|---------|
| Returns | One value, then function **ends** | One value, then function **pauses** |
| State | Destroyed after return | **Preserved** between calls |
| Resumable | ❌ No | ✅ Yes |
| Memory | Builds full result | One value at a time |
| Multiple values | ❌ Only once | ✅ Many times |

```python
def demo():
    print("Before first yield")
    yield 1
    print("Before second yield")
    yield 2
    print("Before third yield")
    yield 3

gen = demo()
print(next(gen))   # Before first yield  →  1
print(next(gen))   # Before second yield →  2
print(next(gen))   # Before third yield  →  3
```

> After each `yield`, the function **pauses** — all local variables and the execution position are saved. The next `next()` call resumes from exactly where it left off.

### Basic Example

```python
def get_chai():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai()

print(next(chai))   # Cup 1
print(next(chai))   # Cup 2
print(next(chai))   # Cup 3
print(next(chai))   # ❌ StopIteration — no more values
```

### `yield` inside a loop

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)   # 5  4  3  2  1
```

```python
def squares(n):
    for x in range(1, n + 1):
        yield x ** 2

for s in squares(5):
    print(s)   # 1  4  9  16  25
```

---

## `next()`

`next()` resumes the generator and returns the next yielded value. When the generator is exhausted, it raises `StopIteration`.

```python
gen = (x ** 2 for x in range(3))

print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4
print(next(gen))   # ❌ StopIteration
```

### Safe `next()` with a default

Pass a second argument to avoid `StopIteration`:

```python
gen = (x for x in range(2))

print(next(gen, "done"))   # 0
print(next(gen, "done"))   # 1
print(next(gen, "done"))   # done  ← no error
```

### Safe iteration with `for`

A `for` loop handles `StopIteration` automatically — it stops cleanly when the generator is exhausted.

```python
chai = get_chai()

for cup in chai:
    print(cup)

# Cup 1
# Cup 2
# Cup 3
```

---

## Infinite Generator

An infinite generator produces values forever. Always control it with `next()`, a counter, or a `break`.

```python
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = natural_numbers()
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3
```

```python
# Take only the first 5 values
first_five = [next(gen) for _ in range(5)]
print(first_five)   # [4, 5, 6, 7, 8]  (continues from where gen left off)
```

```python
# Infinite even number generator
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

evens = even_numbers()
for _ in range(5):
    print(next(evens))   # 0  2  4  6  8
```

> Never use `for item in infinite_gen()` without a `break` — it will run forever.

---

## `send()`

`.send()` is like `next()`, but it also **passes a value into the generator**. The sent value becomes the result of the `yield` expression inside the function.

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # sends total out, receives value in
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)            # prime — advance to the first yield
print(gen.send(10))  # 10
print(gen.send(20))  # 30
print(gen.send(5))   # 35
```

### How `send()` works step by step

1. `next(gen)` — generator starts, hits `yield total` (total=0), pauses, returns `0`
2. `gen.send(10)` — `10` is received as `value`, `total` becomes `10`, hits `yield total`, returns `10`
3. `gen.send(20)` — `20` is received, `total` becomes `30`, returns `30`

> **Important:** You must always call `next(gen)` (or `gen.send(None)`) once first to advance the generator to its first `yield`. Calling `.send()` immediately raises `TypeError`.

```python
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)             # prime
gen.send("hello")     # Received: hello
gen.send("world")     # Received: world
```

---

## `yield from`

`yield from` delegates to another generator or iterable — it forwards all values from the sub-generator, including `send()` values and exceptions.

### Basic usage — replacing a loop

```python
# Without yield from — verbose
def combined():
    for x in gen1():
        yield x
    for x in gen2():
        yield x

# With yield from — clean
def combined():
    yield from gen1()
    yield from gen2()
```

### Real example — chai menu

```python
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)
```

**Output:**
```
Masala Chai
Ginger Chai
Matcha
Oolong
```

### `yield from` with any iterable

`yield from` works on lists, tuples, strings, ranges — not just generators:

```python
def chai_menu():
    yield from ["Masala Chai", "Elaichi Chai", "Ginger Chai"]

def spell_out():
    yield from "chai"   # yields 'c', 'h', 'a', 'i' one by one

for c in spell_out():
    print(c)   # c  h  a  i
```

### `yield from` with return values

`yield from` also captures the return value of a sub-generator:

```python
def sub_gen():
    yield 1
    yield 2
    return "sub done"

def main_gen():
    result = yield from sub_gen()   # result = "sub done"
    print(f"Sub generator finished with: {result}")
    yield 3

for val in main_gen():
    print(val)

# 1
# 2
# Sub generator finished with: sub done
# 3
```

---

## `.close()`

`.close()` stops a generator early by throwing a `GeneratorExit` exception inside it. Use it to clean up resources when you're done with a generator before it's exhausted.

```python
def countdown():
    n = 10
    while True:
        yield n
        n -= 1

gen = countdown()
print(next(gen))   # 10
print(next(gen))   # 9
gen.close()        # stop early
print(next(gen))   # ❌ StopIteration — generator is now closed
```

### Handling cleanup with `try/finally`

```python
def managed_resource():
    print("Resource opened")
    try:
        while True:
            yield
    finally:
        print("Resource closed")   # always runs on .close()

gen = managed_resource()
next(gen)       # Resource opened
next(gen)
gen.close()     # Resource closed  ← cleanup guaranteed
```

> Use `.close()` when your generator holds resources (open files, DB connections) and you want to release them before the generator is exhausted.

---

## Generator Expression

A generator expression is the one-line shorthand — uses `( )` instead of `[ ]`.

```python
# List comprehension — builds entire list in memory
squares_list = [x ** 2 for x in range(10)]

# Generator expression — lazy, one value at a time
squares_gen  = (x ** 2 for x in range(10))

print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
```

Pass directly into functions — no intermediate list needed:

```python
total = sum(x ** 2 for x in range(1, 1001))
print(total)   # 333833500
```

---

## Practical Use Cases

### Reading a large file line by line
```python
def read_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("data.txt"):
    print(line)   # one line at a time — never loads whole file
```

### Paginating results
```python
def paginate(data, page_size):
    for i in range(0, len(data), page_size):
        yield data[i : i + page_size]

records = list(range(1, 21))

for page in paginate(records, 5):
    print(page)

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
```

### Infinite Fibonacci sequence
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_ten = [next(fib) for _ in range(10)]
print(first_ten)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Generator vs List vs Iterator

| | List | Generator Function | Generator Expression |
|---|------|-------------------|---------------------|
| Syntax | `[...]` | `def fn(): yield` | `(...)` |
| Memory | All at once | One at a time | One at a time |
| Reusable | ✅ Yes | ✅ Yes (call again) | ❌ No (exhausted) |
| Infinite sequences | ❌ No | ✅ Yes | ✅ Yes |
| Random access | ✅ `lst[i]` | ❌ No | ❌ No |
| Speed (large data) | Slow | Fast | Fast |
| `.send()` support | ❌ No | ✅ Yes | ❌ No |
| `.close()` support | ❌ No | ✅ Yes | ✅ Yes |

---

## Common Mistakes

### 1. Calling `next()` after exhaustion
```python
gen = (x for x in range(2))
next(gen)   # 0
next(gen)   # 1
next(gen)   # ❌ StopIteration

# ✅ Use a default
next(gen, None)   # None — safe
```

### 2. Reusing an exhausted generator
```python
gen = (x for x in range(3))
list(gen)   # [0, 1, 2]
list(gen)   # [] ← exhausted — call the function again to get a fresh generator
```

### 3. Forgetting to prime before `.send()`
```python
def gen():
    value = yield
    yield value * 2

g = gen()
# g.send(5)   # ❌ TypeError — must prime first
next(g)       # ✅ prime it
print(g.send(5))   # 10
```

### 4. Iterating an infinite generator without a stop condition
```python
def infinite():
    while True:
        yield 1

# ❌ Runs forever — hangs your program
for x in infinite():
    print(x)

# ✅ Always use a limit
gen = infinite()
for _ in range(5):
    print(next(gen))
```

---

## Quick Reference

```python
# Generator function
def gen():
    yield value

# Infinite generator
def infinite():
    while True:
        yield value
        n += 1

# Generator expression
gen = (expr for item in iterable)

# Consume safely with for loop
for item in gen_function():
    print(item)

# Get one value safely
value = next(gen, default)

# First N values from infinite generator
[next(gen) for _ in range(n)]

# Send a value in
next(gen)          # prime first
gen.send(value)

# Delegate to sub-generator
def combined():
    yield from gen1()
    yield from gen2()

# Close early
gen.close()

# Sum without intermediate list
total = sum(x**2 for x in range(1000))
```