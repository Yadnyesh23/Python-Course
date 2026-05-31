# Generator Expression
 
**Syntax:**
```python
(expression for item in iterable)
(expression for item in iterable if condition)
```
 
A generator expression looks like a list comprehension but uses `( )` instead of `[ ]`. The key difference is that it is **lazy** — it computes values one at a time on demand, instead of building the entire list in memory.
 
### Basic Example
```python
# List comprehension — creates entire list in memory immediately
squares_list = [x ** 2 for x in range(10)]
 
# Generator expression — computes one value at a time, on demand
squares_gen  = (x ** 2 for x in range(10))
 
print(squares_list)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares_gen)    # <generator object <genexpr> at 0x...>
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
```
 
### Use Directly in Functions
Generators can be passed directly into functions like `sum()`, `max()`, `min()` — no need to create a list first.
 
```python
numbers = range(1, 1000001)
 
# Memory efficient — no intermediate list created
total = sum(x ** 2 for x in numbers if x % 2 == 0)
print(total)
```
 
### Real-life Example — Process a large file line by line
```python
# Instead of loading the whole file into a list:
lines = (line.strip() for line in open("data.txt"))
 
for line in lines:
    print(line)   # processes one line at a time
```

### List vs Generator
 
| | List Comprehension | Generator Expression |
|---|-------------------|---------------------|
| Syntax | `[...]` | `(...)` |
| Returns | Full list in memory | Lazy iterator |
| Memory | High (all at once) | Low (one at a time) |
| Reusable | ✅ Yes | ❌ No (exhausted after one pass) |
| Speed (small data) | Slightly faster | Slightly slower |
| Speed (large data) | Slower | Faster |
| Best for | Small collections, multiple reuse | Large/infinite data streams |
 
> Use a **generator** when you only need to iterate once and the data is large. Use a **list** when you need random access or will iterate multiple times.