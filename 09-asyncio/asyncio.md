# Asyncio

## Core Concepts

| Term | Description |
|------|-------------|
| `coroutine` | A special function that can pause and resume its execution |
| `async def` | Declares a coroutine function |
| `await` | Pauses execution inside a coroutine until a result is ready |
| `asyncio` | Python's built-in library for asynchronous I/O |
| **Event loop** | The engine that runs and schedules coroutines |

### Blocking vs Non-Blocking

```python
# Blocking — halts the entire program
time.sleep(2)

# Non-Blocking — pauses only the current coroutine
await asyncio.sleep(2)
```

---

## Mixing Threads with Asyncio

Use `ThreadPoolExecutor` + `loop.run_in_executor()` to run blocking/synchronous code without blocking the event loop.

```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item: str) -> str:
    """Synchronous, blocking function (e.g. a legacy DB call)."""
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} stock: 42"

async def main() -> None:
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())
```

> **When to use this:** Any time you need to call blocking I/O or CPU-bound synchronous code from inside an `async` context.

---

## Mixing Multiprocessing with Asyncio

Use `ProcessPoolExecutor` for CPU-bound work (bypasses the GIL).

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy_task(n: int) -> int:
    """Pure CPU work — benefits from a separate process."""
    return sum(i * i for i in range(n))

async def main() -> None:
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_heavy_task, 10_000_000)
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

> **When to use this:** CPU-intensive tasks like image processing, number crunching, or ML inference — where threading won't help due to the GIL.

---

## Quick Reference

| Executor | Use case | Bypasses GIL? |
|---|---|---|
| `ThreadPoolExecutor` | Blocking I/O (network, file, DB) | No |
| `ProcessPoolExecutor` | CPU-bound computation | Yes |