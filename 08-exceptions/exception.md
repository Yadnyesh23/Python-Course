# Exception Handling in Python

Exception handling allows a program to deal with errors gracefully instead of crashing.

Without exception handling:

```python
num = int(input("Enter a number: "))
print(10 / num)
```

If the user enters text or `0`, the program crashes.

With exception handling, we can catch and handle these errors.

---

# What is an Exception?

An exception is an error that occurs while the program is running.

Examples:

```python
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
```

Example:

```python
print(10 / 0)
```

Output:

```python
ZeroDivisionError: division by zero
```

---

# Try-Except

The `try` block contains code that might cause an exception.

The `except` block handles the exception.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except:
    print("Something went wrong")
```

Instead of crashing, the program displays a message.

---

# Catching Specific Exceptions

It is better to catch specific exceptions rather than using a generic `except`.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Multiple Exceptions

A single block can handle multiple exceptions.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

You can also use multiple `except` blocks.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Exception Object

The exception can be stored in a variable.

```python
try:
    print(10 / 0)

except ZeroDivisionError as e:
    print("Error:", e)
```

Output:

```python
Error: division by zero
```

---

# Else Block

The `else` block executes only if no exception occurs.

```python
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

else:
    print("You entered:", num)
```

Flow:

```text
No Exception
    ↓
Else Executes

Exception
    ↓
Except Executes
```

---

# Finally Block

The `finally` block always executes.

```python
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Finished")
```

Output:

```python
5.0
Program Finished
```

Common use:

- Closing files
- Closing database connections
- Cleaning resources

---

# Raising Exceptions

Sometimes Python does not automatically raise an error, but we want to create one ourselves.

Use `raise`.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```python
ValueError: Age cannot be negative
```

---

# Why Use Raise?

To enforce business rules and validations.

Example:

```python
balance = 500

withdraw = 1000

if withdraw > balance:
    raise ValueError("Insufficient Balance")
```

---

# Custom Exceptions

Python allows us to create our own exception classes.

Syntax:

```python
class MyError(Exception):
    pass
```

Custom exceptions should inherit from `Exception`.

---

# Example: OutOfIngredients Exception

```python
class OutOfIngredients(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredients("Missing milk or sugar")

    print("Chai is ready")
```

Usage:

```python
try:
    make_chai(0, 2)

except OutOfIngredients as e:
    print(e)
```

Output:

```python
Missing milk or sugar
```

---

# Example: Insufficient Balance Exception

```python
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Withdrawal amount exceeds balance"
        )

    return balance - amount
```

Usage:

```python
try:
    withdraw(1000, 1500)

except InsufficientBalanceError as e:
    print(e)
```

Output:

```python
Withdrawal amount exceeds balance
```

---

# Exception Hierarchy

```text
BaseException
    │
    ├── SystemExit
    ├── KeyboardInterrupt
    │
    └── Exception
          │
          ├── ValueError
          ├── TypeError
          ├── IndexError
          ├── KeyError
          ├── ZeroDivisionError
          └── Custom Exceptions
```

Custom exceptions should inherit from:

```python
Exception
```

not:

```python
BaseException
```

---

# Best Practices

### Catch Specific Exceptions

✅ Good

```python
except ValueError:
```

❌ Avoid

```python
except:
```

---

### Use Meaningful Error Messages

✅ Good

```python
raise ValueError("Age cannot be negative")
```

❌ Avoid

```python
raise ValueError("Error")
```

---

### Create Custom Exceptions for Business Logic

```python
class OutOfIngredients(Exception):
    pass
```

Makes code more readable and maintainable.

---

### Don't Suppress Errors Silently

❌ Bad

```python
try:
    risky_code()

except:
    pass
```

This hides problems and makes debugging difficult.

---

# Interview Definitions

### Exception

An event that interrupts the normal flow of a program due to an error.

### try

Contains code that may raise an exception.

### except

Handles an exception if one occurs.

### else

Executes only when no exception occurs.

### finally

Executes regardless of whether an exception occurs.

### raise

Used to manually trigger an exception.

### Custom Exception

A user-defined exception class that inherits from `Exception`.

---

# Quick Summary

| Keyword | Purpose |
|----------|----------|
| try | Code that may fail |
| except | Handle errors |
| else | Runs if no error occurs |
| finally | Always runs |
| raise | Create an exception manually |
| Exception | Base class for most errors |
| Custom Exception | User-defined error type |

## Remember

- Use `try-except` to prevent crashes.
- Catch specific exceptions whenever possible.
- Use `raise` to enforce rules and validations.
- Create custom exceptions for meaningful business errors.
- `finally` always runs.
- `else` runs only when no exception occurs.