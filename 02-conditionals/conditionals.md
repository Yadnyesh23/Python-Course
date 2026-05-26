# Conditionals in Python

Conditionals allow your program to make decisions — executing different blocks of code depending on whether a condition is `True` or `False`.

---

## if / elif / else

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

**Output:**
```
Adult
```

### Rules
- `if` — required, always comes first
- `elif` — optional, can have as many as needed
- `else` — optional, catches everything that didn't match above
- Only the **first matching block** executes; the rest are skipped

---

## `input()` — int vs str

```python
income = input("Enter your income : ")      # returns a STRING "50000"
income = int(input("Enter your income : ")) # returns an INTEGER 50000
```

> By default, `input()` always returns a **string**, even if the user types a number. You must explicitly convert it using `int()`, `float()`, etc. — otherwise comparisons like `income > 30000` will raise a `TypeError`.

```python
# Without conversion — bug
income = input("Enter your income : ")  # user types 50000
if income > 30000:                      # ❌ TypeError: '>' not supported between str and int
    print("High income")

# With conversion — correct
income = int(input("Enter your income : "))
if income > 30000:                      # ✅ works fine
    print("High income")
```

---

## Comparison Operators

Used inside conditions to compare values:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `age != 18` |
| `>` | Greater than | `age > 18` |
| `<` | Less than | `age < 18` |
| `>=` | Greater than or equal | `age >= 18` |
| `<=` | Less than or equal | `age <= 18` |

---

## Logical Operators

Combine multiple conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `age > 18 and age < 60` |
| `or` | At least one must be True | `day == "Sat" or day == "Sun"` |
| `not` | Inverts the condition | `not is_raining` |

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

---

## Truthy and Falsy in Conditions

Python evaluates non-boolean values as `True` or `False` in conditions:

| Falsy (treated as False) | Truthy (treated as True) |
|--------------------------|--------------------------|
| `0`, `0.0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `[]`, `{}`, `()` | Any non-empty collection |
| `None` | Any object |
| `False` | `True` |

```python
name = ""

if name:
    print(f"Hello, {name}")
else:
    print("Name is empty")   # This runs because "" is falsy
```

---

## Inline Condition (Ternary Operator)

A one-line shorthand for simple `if-else`:

**Syntax:**
```python
value = <result_if_true> if <condition> else <result_if_false>
```

```python
order_amount = 250

delivery_charge = 0 if order_amount >= 300 else 30
print(f"Delivery charge : ₹{delivery_charge}")  # ₹30
```

```python
# More examples
age    = 20
status = "Adult" if age >= 18 else "Minor"

score  = 75
grade  = "Pass" if score >= 50 else "Fail"

number = -5
label  = "Positive" if number > 0 else "Zero" if number == 0 else "Negative"
```

> Keep ternary operators simple. If the logic is complex, use a regular `if-else` block for readability.

---

## Nested Conditions

Conditions inside conditions:

```python
income = 75000
age    = 30

if age >= 18:
    if income >= 50000:
        print("Eligible for premium loan")
    else:
        print("Eligible for basic loan")
else:
    print("Not eligible — must be 18+")
```

> Avoid deep nesting (more than 2 levels) — it makes code hard to read. Use `and` / `or` to flatten where possible.

```python
# Nested version (harder to read)
if age >= 18:
    if income >= 50000:
        print("Eligible for premium loan")

# Flattened version (cleaner)
if age >= 18 and income >= 50000:
    print("Eligible for premium loan")
```

---

## `in` and `not in` in Conditions

Check membership inside a condition:

```python
cities  = ["Mumbai", "Pune", "Thane"]
city    = "Pune"

if city in cities:
    print(f"{city} is in the list")

blocked = ["admin", "root", "superuser"]
username = "guest"

if username not in blocked:
    print("Access granted")
```

---

## `is` vs `==`

| Operator | Checks |
|----------|--------|
| `==` | Whether two values are **equal** |
| `is` | Whether two variables point to the **same object in memory** |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  → same value
print(a is b)   # False → different objects in memory
print(a is c)   # True  → c points to the same object as a
```

> Use `==` for value comparison. Use `is` only for checking identity — most commonly `is None`.

```python
value = None

if value is None:       # ✅ correct way to check for None
    print("No value set")

if value == None:       # ⚠️ works but not recommended
    print("No value set")
```

---

## match-case (Python 3.10+)

`match-case` is Python's version of a switch statement — cleaner than long `if-elif` chains when matching a variable against specific values.

**Syntax:**
```python
match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default (like else)
```

```python
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend — no work!")
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost the weekend!")
    case _:
        print("Regular weekday")
```

**Output:**
```
Start of the week
```

### match-case with conditions (guards)

You can add an `if` guard to a case for extra filtering:

```python
score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 75:
        print("Grade: B")
    case s if s >= 50:
        print("Grade: C")
    case _:
        print("Grade: F")
```

### match-case vs if-elif

| | `if-elif` | `match-case` |
|---|-----------|--------------|
| Available since | All versions | Python 3.10+ |
| Best for | Range checks, complex logic | Matching exact values |
| Supports guards (`if`) | Always | Yes (with `case x if ...`) |
| Readability | Good | Better for many exact values |