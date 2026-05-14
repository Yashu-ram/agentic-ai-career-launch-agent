# Career Launch Agent

An AI/Agentic AI project setup using Python, uv, JupyterLab, and Git.

---

## Project Setup

### 1. Create Virtual Environment

```bash
uv venv
```

### 2. Activate Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
uv sync
```

---

### 4. Run JupyterLab

```bash
jupyter lab
```

---

## Project Structure

```text
career-launch-agent/
│
├── .venv/
├── README.md
├── pyproject.toml
├── uv.lock
├── sanity_check.ipynb
└── .gitignore
```

---

## Sanity Check

Run the notebook:

```python
import json
import os
from pathlib import Path

print("Hello Agentic AI")
```

Expected output:

```text
Hello Agentic AI
```

---

## Git Setup

Initialize repository:

```bash
git init
git add .
git commit -m "initial setup"
```

---

## Tech Stack

- Python 3.11+
- uv
- JupyterLab
- Git
- VS Code