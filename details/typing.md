mypy is a static type checker for Python that analyzes your code before runtime to catch type-related errors. It uses Python type hints to ensure your functions, variables, and return values follow expected types, similar to how TypeScript checks JavaScript.

Example:
pip install mypy

def add(a: int, b: int) -> int:
    return a + b

add(5, "10")  # ❌ MyPy will flag this as a type error
run your file - mypy your_file.py


pyright is a fast static type checker developed by Microsoft, designed for large Python codebases. It’s commonly used in VS Code and focuses on speed, strict type checking, and excellent editor integration. It is written in Nodejs and can be installed by vscode extension or by npm

Example:
def greet(name: str) -> str:
    return "Hello " + name

greet(123)  # ❌ Pyright will immediately flag this in the editor
🧠 Simple difference


MyPy → traditional, widely used, very strict batch checking
Pyright → faster, editor-first, great real-time feedback (VS Code friendly)