# Strings

Strings are **immutable** — once created, their characters cannot be changed in place. Anything wrapped in `" "` or `' '` is a string.

---

## Indexing & Slicing

Every character in a string has a numeric index, starting from `0`.

```
 A  r  o  m  a  t  i  c     a  n  d     B  o  l  d
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
```

**Syntax:**
```python
variable[start : end : step]
```

- `start` — index to begin at (inclusive). Defaults to `0`.
- `end` — index to stop at (exclusive). Defaults to end of string.
- `step` — how many characters to skip. Defaults to `1`.

```python
description = "Aromatic and Bold"

print(description[0:8])    # Aromatic       → characters from index 0 to 7
print(description[:8])     # Aromatic       → same as above, start defaults to 0
print(description[:8:2])   # Aoai           → every 2nd character from 0 to 7
print(description[:8:3])   # Ami            → every 3rd character from 0 to 7
print(description[13:])    # Bold           → from index 13 to end
print(description[::-1])   # dloB dna citamorA → reverse the entire string
```

**Output:**
```
Aromatic
Aromatic
Aoai
Ami
Bold
dloB dna citamorA
```

> **Tip:** A negative step (`-1`) reverses the string. `[::-1]` is the standard Python idiom for reversing any sequence.

---

## Encoding & Decoding

Encoding converts a string into **bytes** (raw binary data) for storage or transmission. Decoding converts it back to a readable string.

```python
label_text   = "Chai spécial"
encoded_text = label_text.encode("utf-8")    # str  → bytes
decoded_text = encoded_text.decode("utf-8")  # bytes → str

print(f"Original : {label_text}")
print(f"Encoded  : {encoded_text}")
print(f"Decoded  : {decoded_text}")
```

**Output:**
```
Original : Chai spécial
Encoded  : b'Chai sp\xc3\xa9cial'
Decoded  : Chai spécial
```

> **Why encoding?** The special character `é` cannot be represented in plain ASCII, so UTF-8 encodes it as two bytes: `\xc3\xa9`. Decoding reverses this process perfectly.