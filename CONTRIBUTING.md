# Contributing to PyStructures

Thank you for your interest in contributing to **PyStructures**!  
This document will help you get started as a contributor, set up your development environment, and understand our code and collaboration standards.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Pull Requests](#pull-requests)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)
- [License](#license)
- [Contact](#contact)

---

## Getting Started

1. **Fork** the repository on GitHub and clone your fork locally.
2. Make sure you have Python **3.9+** installed.
3. Install development dependencies.

---

## Development Setup

Install dev dependencies (for testing and coverage):

```bash
pip install -e .[dev]
```

---

## Running Tests

Automated tests are located in the `tests/` directory.

- To run all tests from the project root:
  ```bash
  python -m pytest
  ```
  or
  ```bash
  pytest
  ```

- To run tests for a specific category:
  ```bash
  pytest tests/linear/
  ```

- To check test coverage:
  ```bash
  python -m pytest --cov=pystructures
  ```
  or
  ```bash
  pytest --cov=pystructures
  ```

- To generate an HTML coverage report:
  ```bash
  python -m pytest --cov=pystructures --cov-report=html
  ```
  Then open `htmlcov/index.html` in your browser.

**Please make sure all tests pass before submitting a pull request.**

---

## Code Style

- Follow [PEP8](https://peps.python.org/pep-0008/) for Python code style.
- Use meaningful variable and function names.
- Organize code logically in the `pystructures/` package (`linear`, `nonlinear`, `unordered`).
- Add docstrings to all classes and methods.

---

## Documentation

- Update or create documentation for new data structures or significant changes.
- Documentation files are located in the `docs/` directory.
- Each new class should have usage examples, method descriptions, and complexity analysis in its Markdown file.

---

## Pull Requests

- Make sure your branch is up to date with `master` before submitting a PR.
- Fill out the PR template if available.
- Describe what your change does and why it's needed.
- Reference related issues if applicable.
- Ensure added code is covered by tests.

---

## Reporting Issues

- Use [GitHub Issues](https://github.com/0xV4h3/PyStructures/issues) for bugs, questions, or suggestions.
- Include as much detail as possible: steps to reproduce, expected behavior, environment info, etc.

---

## Feature Requests

- Open an issue with a clear description of your proposed feature.
- Explain the use case and why it would be valuable.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions, reach out via [GitHub](https://github.com/0xV4h3) or open an issue.
