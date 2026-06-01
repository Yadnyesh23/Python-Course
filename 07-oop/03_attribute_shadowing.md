# Attribute Shadowing in Python

## What is Attribute Shadowing?

Attribute shadowing happens when an **instance attribute has the same name as a class attribute**. The instance attribute takes priority — it "shadows" the class attribute for that specific object. The class attribute itself is not modified; it still exists and is accessible via the class or other instances.

```
Lookup order: instance namespace → class namespace → parent class → AttributeError
```

---

## How Shadowing Works

```python
class Chai:
    temperature = "hot"     # class attribute — shared by all instances
    strength    = "strong"

cutting = Chai()

# Before shadowing — instance has no 'temperature', so it reads from the class
print(f"Before shadowing : {cutting.temperature}")   # hot

# Assigning creates a NEW entry in the INSTANCE namespace — shadows the class attribute
cutting.temperature = "mild"
print(f"After shadowing  : {cutting.temperature}")   # mild  ← instance value

# The class attribute is untouched
print(f"Class attribute  : {Chai.temperature}")      # hot   ← unchanged
```

**Output:**
```
Before shadowing : hot
After shadowing  : mild
Class attribute  : hot
```

---

## Deleting a Shadowed Attribute — Fallback to Class

When you `del` an instance attribute, the instance's own namespace entry is removed. Python then falls back to the **class attribute** on the next lookup.

```python
del cutting.temperature
print(f"After deleting instance attr : {cutting.temperature}")   # hot  ← falls back to class
```

> Deleting `cutting.temperature` only removes the instance's copy. The class attribute `Chai.temperature = "hot"` was never touched, so it reappears.

---

## Deleting an Attribute with No Class Fallback

If you add an attribute directly to an instance (one that doesn't exist on the class), deleting it leaves nothing to fall back on — Python raises an `AttributeError`.

```python
cutting.cup = "full"   # new attribute — exists ONLY on the instance, not on the class
print(f"Before deleting : {cutting.cup}")   # full

del cutting.cup
print(f"After deleting  : {cutting.cup}")   # ❌ AttributeError — no class fallback
```

> `cup` was never defined on `Chai`, so there is nothing to fall back to after deletion.

---

## Full Example

```python
class Chai:
    temperature = "hot"
    strength    = "strong"

cutting = Chai()

# Step 1 — reads from class (no instance attribute yet)
print(f"Before shadowing : {cutting.temperature}")    # hot

# Step 2 — creates instance attribute, shadows class
cutting.temperature = "mild"
print(f"After shadowing  : {cutting.temperature}")    # mild

# Step 3 — delete instance attribute, fallback to class
del cutting.temperature
print(f"After deleting   : {cutting.temperature}")    # hot  ← class fallback

# Step 4 — instance-only attribute (no class equivalent)
cutting.cup = "full"
print(f"Before deleting  : {cutting.cup}")            # full

# Step 5 — delete it — nothing to fall back to
del cutting.cup
print(f"After deleting   : {cutting.cup}")            # ❌ AttributeError
```

**Output:**
```
Before shadowing : hot
After shadowing  : mild
After deleting   : hot
Before deleting  : full
AttributeError: 'Chai' object has no attribute 'cup'
```

---

## Inspecting Namespaces

You can check what's in each namespace at any time using `__dict__`:

```python
class Chai:
    temperature = "hot"

cutting = Chai()

print(Chai.__dict__)     # {'temperature': 'hot', ...}  ← class namespace
print(cutting.__dict__)  # {}  ← instance namespace is empty

cutting.temperature = "mild"
print(cutting.__dict__)  # {'temperature': 'mild'}  ← now has its own entry

del cutting.temperature
print(cutting.__dict__)  # {}  ← instance entry removed; class still has it
```

---

## Summary

| Situation | Result |
|-----------|--------|
| Instance has no attribute → access | Reads from class attribute |
| Instance attribute set | Shadows the class attribute for this object only |
| Instance attribute deleted, class has it | Falls back to class attribute |
| Instance attribute deleted, class does NOT have it | `AttributeError` |
| Class attribute modified via `Chai.attr = x` | Affects all instances that haven't shadowed it |

> Shadowing never modifies the class. It only adds or removes entries in the **instance's own namespace**.