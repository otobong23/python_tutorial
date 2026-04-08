## Python `venv` (Virtual Environment)

A **virtual environment (`venv`)** in Python is an isolated workspace that allows you to manage project dependencies separately from the global Python installation.

Each project can have its own versions of packages without affecting other projects or the system-wide Python setup. This helps prevent version conflicts and keeps projects reproducible.

### How it works

When you create a `venv`, Python creates a local directory containing:

* A copy of the Python interpreter
* A separate `site-packages` folder for installed libraries
* Activation scripts for enabling the environment

Once activated, any `pip install` command installs packages only inside that environment.

### Key Benefit

`venv` ensures that each Python project behaves like an independent ecosystem, similar to how `node_modules` works in Node.js projects.

### Basic Usage

```bash
python -m venv my_env
```
General Conventions names for "my_env" are venv, .venv

Activate:

* Windows: `my_env\Scripts\activate`
* Mac/Linux: `source my_env/bin/activate`

---

In summary, `venv` keeps Python projects clean, isolated, and dependency-safe.
