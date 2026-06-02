# Method Resolution Order (MRO)

Method Resolution Order (MRO) defines the order in which Python searches for attributes and methods in a class hierarchy, especially when multiple inheritance is involved.

## Example

```python
class A:
    label = "A: Base Class"


class B(A):
    label = "B: Masala Blend"


class C(A):
    label = "C: Ginger Blend"


class D(C, B):
    pass


cup = D()

print(cup.label)
print(D.__mro__)
```

## Output

```python
C: Ginger Blend

(<class '__main__.D'>,
 <class '__main__.C'>,
 <class '__main__.B'>,
 <class '__main__.A'>,
 <class 'object'>)
```

## Explanation

When `cup.label` is accessed, Python follows the MRO of class `D`:

1. `D`
2. `C`
3. `B`
4. `A`
5. `object`

Since `label` is found in class `C`, Python stops searching and returns:

```python
"C: Ginger Blend"
```

## Key Takeaway

For the class definition:

```python
class D(C, B):
    pass
```

Python searches for attributes and methods in the following order:

```text
D → C → B → A → object
```

The first matching attribute or method found in this order is used.