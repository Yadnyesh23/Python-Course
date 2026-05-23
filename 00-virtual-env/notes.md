# Python Virtual Environments

## The Problem

When working on multiple Python projects, each project may require different versions of the same package. Installing everything globally leads to version conflicts and a messy, hard-to-manage setup.

## What is a Virtual Environment?

A virtual environment is an **isolated Python environment** — a self-contained folder that holds its own Python interpreter and packages, completely separate from your system-wide Python installation.

Think of it as a clean room for each project: whatever you install inside it stays inside it.

## How It Solves the Problem

Each project gets its own virtual environment with its own set of dependencies. Project A can use `requests==2.28` while Project B uses `requests==2.31` — no conflicts, no interference.

## Why You Need It

- Keeps project dependencies **isolated and reproducible**
- Prevents "it works on my machine" issues
- Makes it easy to share projects (via `requirements.txt`)
- Keeps your global Python installation clean

## Advantages

- **Isolation** — packages installed in one venv don't affect others
- **Reproducibility** — freeze exact versions with `pip freeze > requirements.txt`
- **No admin rights needed** — install packages without system-level permissions
- **Easy cleanup** — just delete the folder to remove all dependencies

## Disadvantages

- Takes up disk space (each venv has its own copy of packages)
- You must remember to activate it before working
- Not shared across projects (intentional, but worth noting)

---

## Setting Up a Virtual Environment

### 1. Navigate to your project folder

```bash
cd your-folder-name
```

### 2. Create the virtual environment

```bash
python -m venv .venv
```

> `.venv` is the conventional name. The dot prefix hides it on Unix systems. You can use any name, but stick to `.venv` for consistency.

### 3. Activate it

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

> Once activated, your terminal prompt will show `(.venv)` — this confirms you're inside the environment.

### 4. Install packages (while activated)

```bash
pip install package-name
```

### 5. Save your dependencies

```bash
pip freeze > requirements.txt
```

### 6. Deactivate when done

```bash
deactivate
```

---

## Restoring a venv from `requirements.txt`

If someone else clones your project (or you set it up on a new machine):

```bash
python -m venv .venv
.venv\Scripts\activate        # or: source .venv/bin/activate
pip install -r requirements.txt
```

---

## What to Add to `.gitignore`

Never commit your virtual environment to Git — it's large and machine-specific:

```
.venv/
```

Commit `requirements.txt` instead.

---

> **⚠️ Golden Rule:** Always activate your virtual environment before installing packages or running your project. If you see `(venv)` or `(.venv)` in your terminal prompt, you're good to go.