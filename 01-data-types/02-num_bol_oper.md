# Numbers, Booleans and Operators

## Types of Numbers

Python supports four numeric types:

- **Integer** — whole numbers (e.g. `10`, `-3`)
- **Boolean** — `True` or `False` (a subtype of integer)
- **Float** — decimal numbers (e.g. `3.14`, `95.5`)
- **Complex** — numbers with a real and imaginary part (e.g. `3 + 4j`)

---

## Operators

| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | True Division | `a / b` |
| `//` | Floor Division | `a // b` |
| `%` | Modulus (Remainder) | `a % b` |
| `**` | Exponentiation | `a ** b` |
| `and` | Logical AND | `a and b` |
| `or` | Logical OR | `a or b` |
| `not` | Logical NOT | `not a` |

> **Note:** Python uses `and`, `or`, `not` — not `&&`, `||`, `!` like some other languages.

---

## Integer Operations

```python
a = 10
b = 5

result_sum        = a + b
result_diff       = a - b
result_product    = a * b
result_division   = a / 3       # True division → float
result_floor_div  = a // 3      # Floor division → integer
result_remainder  = a % b
result_power      = a ** b

print(f"Sum of 10 and 5          : {result_sum}")
print(f"Difference of 10 and 5   : {result_diff}")
print(f"Multiplication of 10 × 5 : {result_product}")
print(f"True division of 10 / 3  : {result_division}")
print(f"Floor division of 10 // 3: {result_floor_div}")
print(f"Remainder of 10 % 5      : {result_remainder}")
print(f"10 to the power of 5     : {result_power}")
```

**Output:**
```
Sum of 10 and 5          : 15
Difference of 10 and 5   : 5
Multiplication of 10 × 5 : 50
True division of 10 / 3  : 3.3333333333333335
Floor division of 10 // 3: 3
Remainder of 10 % 5      : 0
10 to the power of 5     : 100000
```

> **True division (`/`)** always returns a float. **Floor division (`//`)** discards the decimal and returns an integer.

---

## Booleans

Booleans have only two values: `True` and `False`.

### Booleans are Integers Under the Hood

```python
a = True
b = 5
print(a + b)  # Output: 6
```

> `True` is treated as `1` and `False` as `0`. This is called **upcasting**.

### Truthy and Falsy Values

```python
milk_present = 0
print(bool(milk_present))  # Output: False
```

In Python, any value is considered **truthy** or **falsy**:

| Falsy | Truthy |
|-------|--------|
| `0` | Any non-zero number |
| `None` | Any non-empty string |
| `""` (empty string) | Any non-empty list, dict, etc. |
| `[]`, `{}`, `()` | `True` |

### Boolean Operators

```python
and   # True if both are true
or    # True if at least one is true
not   # Inverts the boolean value
```

---

## Floats / Decimals

```python
initial_temp = 95.5
final_temp   = 95.49999999999999

print(f"Initial temp : {initial_temp}")
print(f"Final temp   : {final_temp}")
print(f"Difference   : {initial_temp - final_temp}")
```

**Output:**
```
Initial temp : 95.5
Final temp   : 95.49999999999999
Difference   : 1.4210854715202004e-14
```

> **Floating point precision:** The result is not exactly `0` because floats are stored in binary, which cannot represent all decimal numbers with perfect precision. This is a known limitation in most programming languages, not a Python bug.