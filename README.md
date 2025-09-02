# PyStructures

**pystructures** is a collection of classic data structures implemented in Python as clean, easy-to-use classes.  
This project is designed for students, educators, developers, and anyone interested in working with fundamental data structures in Python.

---

## Project Structure

```
PyStructures/
    pystructures/
        __init__.py
        linear/
            __init__.py
            singly_linked_list.py
            doubly_linked_list.py
            stack.py
            queue.py
        nonlinear/
            __init__.py
            binary_tree.py
            binary_search_tree.py
            avl_tree.py
            red_black_tree.py
            heap.py
            priority_queue.py
            trie.py
            splay_tree.py
        unordered/
            __init__.py
            hash_map.py
            hash_set.py
            graph_adjacency_list.py
            graph_adjacency_matrix.py
    docs/
        linear/
            singly_linked_list.md
            doubly_linked_list.md
            stack.md
            queue.md
        nonlinear/
            binary_tree.md
            binary_search_tree.md
            avl_tree.md
            red_black_tree.md
            heap.md
            priority_queue.md
            trie.md
            splay_tree.md
        unordered/
            hash_map.md
            hash_set.md
            graph_adjacency_list.md
            graph_adjacency_matrix.md
    tests/
        linear/
            test_singly_linked_list.py
            test_doubly_linked_list.py
            test_stack.py
            test_queue.py
        nonlinear/
            test_binary_tree.py
            test_binary_search_tree.py
            test_avl_tree.py
            test_red_black_tree.py
            test_heap.py
            test_priority_queue.py
            test_trie.py
            test_splay_tree.py
        unordered/
            test_hash_map.py
            test_hash_set.py
            test_graph_adjacency_list.py
            test_graph_adjacency_matrix.py
    README.md
    LICENSE
    CONTRIBUTING.md
    pyproject.toml
```

---

## Standard & Requirements

- **Python Version:** 3.9+
- **Cross-platform:** Linux, Windows, macOS

---

## Data Structures

### Linear
- `SinglyLinkedList`
- `DoublyLinkedList`
- `Stack`
- `Queue`

### Nonlinear (Hierarchical)
- `BinaryTree`
- `BinarySearchTree`
- `AVLTree`
- `RedBlackTree`
- `SplayTree`
- `Trie`
- `MaxHeap`
- `MinHeap`
- `PriorityQueue`

### Unordered
- `HashMap`
- `HashSet`
- `GraphAdjacencyList`
- `GraphAdjacencyMatrix`

---

## Documentation

Detailed documentation for each data structure is available in the `docs/` directory:

- **Linear**
  - [SinglyLinkedList](docs/linear/singly_linked_list.md)
  - [DoublyLinkedList](docs/linear/doubly_linked_list.md)
  - [Stack](docs/linear/stack.md)
  - [Queue](docs/linear/queue.md)
- **Nonlinear**
  - [BinaryTree](docs/nonlinear/binary_tree.md)
  - [BinarySearchTree](docs/nonlinear/binary_search_tree.md)
  - [AVLTree](docs/nonlinear/avl_tree.md)
  - [RedBlackTree](docs/nonlinear/red_black_tree.md)
  - [MaxHeap, MinHeap](docs/nonlinear/heap.md)
  - [PriorityQueue](docs/nonlinear/priority_queue.md)
  - [Trie](docs/nonlinear/trie.md)
  - [SplayTree](docs/nonlinear/splay_tree.md)
- **Unordered**
  - [HashMap](docs/unordered/hash_map.md)
  - [HashSet](docs/unordered/hash_set.md)
  - [GraphAdjacencyList](docs/unordered/graph_adjacency_list.md)
  - [GraphAdjacencyMatrix](docs/unordered/graph_adjacency_matrix.md)

Each file contains usage examples, detailed method descriptions, and complexity analysis.

---

## Development Setup

To install development dependencies (for testing and coverage):

```bash
pip install -e .[dev]
```

---

## Tests

Automated tests for each data structure are located in the `tests/` directory, organized by category (`linear`, `nonlinear`, `unordered`), matching the main project structure.

**How to run tests:**  
- Make sure you have [pytest](https://pytest.org/) installed (see Development Setup above).
- Run all tests from the project root (the folder containing `pystructures`, `tests`, and `docs`):

  ```bash
  python -m pytest
  ```
  or, if the package is installed (or in editable mode):

  ```bash
  pytest
  ```

- To run tests for a specific category:

  ```bash
  pytest tests/linear/
  ```

If you contribute code, please add or update tests for your changes.

---

## Test Coverage

To check how much of the code is covered by tests (coverage), install [pytest-cov](https://pytest-cov.readthedocs.io/) as shown above.

Then run all tests with coverage report:

```bash
python -m pytest --cov=pystructures
```
or
```bash
pytest --cov=pystructures
```
If you get an import error, prefer running with `python -m pytest --cov=pystructures`.

To generate a detailed HTML coverage report:

```bash
python -m pytest --cov=pystructures --cov-report=html
```
Open `htmlcov/index.html` in your browser to view the report.

---

## Installation

**Local (add to your project):**

Copy the `pystructures` folder to your project.

**Via pip (after publishing to PyPI):**
```bash
pip install pystructures
```

---

## Usage

Import the required data structures:

```python
from pystructures import Stack, BinaryTree, HashMap
from pystructures.linear import Queue
from pystructures.nonlinear import AVLTree, MaxHeap, MinHeap
from pystructures.unordered import GraphAdjacencyList

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

heap = MaxHeap([5, 3, 8])
heap.push(10)
print(heap.pop())  # Output: 10

minheap = MinHeap([4, 2, 7])
print(minheap.peek())  # Output: 2
```

---

## License

MIT License