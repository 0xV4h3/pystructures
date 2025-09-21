# BinaryTree

A Python implementation of a classic binary tree with a full, modern, Pythonic API.  
Supports arbitrary insertions, multiple traversals, bulk operations, copy/deepcopy, rich comparison, and structural utility methods.

---

## Overview

**BinaryTree** is a hierarchical data structure in which each node has at most two children (left and right).  
Unlike search trees, this implementation does not impose any ordering constraint—children can hold any values.

- **Data type:** Any Python object
- **Operations:** Arbitrary child insertion, removal by value, traversals, bulk extension, copying, comparison, completeness/balance checks
- **Features:** Multiple traversals, bulk construction, copy/deepcopy, equality, height, completeness, balance, degenerate/full/perfect checks

---

## API Reference

### Constructor

```python
BinaryTree(iterable: Optional[Iterable[Any]] = None)
```
Create an empty tree or build from any iterable (level-order).

#### Example
```python
from pystructures.nonlinear import BinaryTree

tree = BinaryTree([1, 2, 3])
print(tree)  # BinaryTree([1, 2, 3])
```

---

### Core Methods

#### `insert_left(parent: BinaryTree._Node, value: Any) -> BinaryTree._Node`
Insert a value as the left child of `parent`. **O(1)**

#### `insert_right(parent: BinaryTree._Node, value: Any) -> BinaryTree._Node`
Insert a value as the right child of `parent`. **O(1)**

#### `extend(iterable: Iterable[Any]) -> None`
Insert all elements from `iterable` in level-order (first available positions). **O(k * n)**

#### `remove(value: Any) -> None`
Remove the first occurrence of `value` in level-order traversal.  
Replaces the removed node with the deepest node to preserve completeness.  
Raises `ValueError` if not found. **O(n)**

#### `find(value: Any) -> Optional[BinaryTree._Node]`
Return a reference to the first node containing `value` in level-order traversal, or `None` if not found. **O(n)**

#### Example
```python
node = tree.find(2)
if node is not None:
    print(node.data)  # 2
else:
    print("Value not found")
```

#### `find_index(value: Any) -> int`
Return the index of the first occurrence of `value` (level-order), or -1 if not found. **O(n)**

#### Example
```python
idx = tree.find_index(2)  # e.g., 1
```

#### `contains(value: Any) -> bool`
Check if value exists in the tree. **O(n)**
  
#### `count(value: Any) -> int`
Count the occurrences of a value in the tree. **O(n)**

#### `copy() -> BinaryTree`
Return a shallow copy of the tree. **O(n)**

#### `clear() -> None`
Remove all nodes from the tree. **O(1)**

#### `is_empty() -> bool`
Return `True` if the tree is empty. **O(1)**

#### `root() -> Optional[BinaryTree._Node]`
Return the root node (or None if tree is empty). **O(1)**

---

### Traversal & Conversion

#### `traverse(order: str = "inorder") -> Iterator[Any]`
Traverse the tree in the specified order.  
Supported orders: `"inorder"`, `"preorder"`, `"postorder"`, `"levelorder"`, `"reverselevelorder"`, `"boundary"`, `"diagonal"`.

#### `to_list(order: str = "inorder") -> list[Any]`
Convert the tree to a list in the specified traversal order.

#### Example
```python
tree = BinaryTree([1, 2, 3, 4])
print(tree.to_list("inorder"))      # [4, 2, 1, 3]
print(tree.to_list("levelorder"))   # [1, 2, 3, 4]
```

#### Iteration

- `__iter__()` – Inorder traversal (default)

---

### Bulk Construction

#### `from_level_order(iterable: Iterable[Any]) -> BinaryTree`
Build a binary tree from an iterable (level-order). **O(n)**

#### Example
```python
tree = BinaryTree.from_level_order([10, 20, 30])
```

---

### Comparison & Equality

#### `__eq__(other: object) -> bool`
Element-wise and structure-wise comparison with another binary tree (based on level-order traversal).

---

### String Representation

#### `__str__()`, `__repr__()`
String representation of the tree.

---

### Utility & Structural Methods

#### `__len__() -> int`
Number of elements in the tree.

#### `height() -> int`
Return the height of the tree. **O(n)**

#### `is_full() -> bool`
Return `True` if every node has either 0 or 2 children. **O(n)**

#### `is_perfect() -> bool`
Return `True` if all leaves are at the same depth, and every node has two children. **O(n)**

#### `is_complete() -> bool`
Return `True` if all levels except possibly the last are full, and the last level is filled left to right. **O(n)**

#### `is_balanced() -> bool`
Return `True` if the tree is height-balanced (difference ≤ 1 for any node). **O(n)**

#### `is_degenerate() -> bool`
Return `True` if each parent has only one child (tree resembles a linked list). **O(n)**

#### `balance() -> None`
Balance the tree by rebuilding as a complete binary tree from the inorder traversal. **O(n)**

---

## Method Overview

| Method        | Args                           | Returns             | Complexity      | Notes                        |
|:--------------|:------------------------------|:--------------------|:---------------|:-----------------------------|
| `insert_left` | `parent, value`               | `_Node`             | O(1)            | Direct child insert          |
| `insert_right`| `parent, value`               | `_Node`             | O(1)            | Direct child insert          |
| `extend`      | `iterable`                    | `None`              | O(k * n)        | Bulk add                     |
| `remove`      | `value`                       | `None`              | O(n)            | Remove by value (level-order)|
| `find`        | `value`                       | `_Node`/`None`      | O(n)            | Node reference (level-order) |
| `find_index`  | `value`                       | `int`               | O(n)            | Level-order index            |
| `contains`    | `value`                       | `bool`              | O(n)            |                             |
| `count`       | `value`                       | `int`               | O(n)            |                             |
| `copy`        | —                             | `BinaryTree`        | O(n)            | Shallow copy                 |
| `clear`       | —                             | `None`              | O(1)            |                             |
| `is_empty`    | —                             | `bool`              | O(1)            |                             |
| `root`        | —                             | `_Node`/None        | O(1)            |                             |
| `traverse`    | `order`                       | `Iterator[Any]`     | O(n)            | Multiple orders supported    |
| `to_list`     | `order`                       | `list[Any]`         | O(n)            |                             |
| `from_level_order` | `iterable`               | `BinaryTree`        | O(n)            | Bulk build                   |
| `__len__`     | —                             | `int`               | O(1)            |                             |
| `height`      | —                             | `int`               | O(n)            |                             |
| `is_full`     | —                             | `bool`              | O(n)            |                             |
| `is_perfect`  | —                             | `bool`              | O(n)            |                             |
| `is_complete` | —                             | `bool`              | O(n)            |                             |
| `is_balanced` | —                             | `bool`              | O(n)            |                             |
| `is_degenerate` | —                           | `bool`              | O(n)            |                             |
| `balance`     | —                             | `None`              | O(n)            |                             |
| `__str__`/`__repr__` | —                      | `str`               | O(n)            |                             |
| `__eq__`      | `other`                       | `bool`              | O(n)            | Level-order comparison       |

---

## Example Usage

```python
from pystructures.nonlinear import BinaryTree

tree = BinaryTree([1, 2, 3, 4])
print(tree.to_list("levelorder"))      # [1, 2, 3, 4]
print(tree.to_list("inorder"))         # [4, 2, 1, 3]

tree.insert_left(tree.root(), 5)
tree.remove(2)
print(2 in tree)                       # False

tree.extend([6, 7])
print(tree.height())                   # e.g., 2

node = tree.find(3)
if node:
    print(node.data)                   # 3
else:
    print("Not found")

idx = tree.find_index(7)
print(idx)                             # e.g., 5

tree.balance()
print(tree.is_balanced())              # True

for x in tree.traverse("preorder"):
    print(x)
```

---

## Notes & Edge Cases

- **All elements** are stored as-is (supports any Python object).
- **Traversal methods** return generators/iterators; use `list()` for a concrete list.
- **Bulk operations:** prefer `extend` or `from_level_order` for efficient construction.
- **Structural queries:** `is_full`, `is_perfect`, `is_complete`, `is_balanced`, `is_degenerate` provide insights into tree shape.
- For advanced usage and custom traversal, see [source code](../../pystructures/nonlinear/binary_tree.py).

---

## See Also

- [BinarySearchTree](binary_search_tree.md) — for ordered trees
- [AVLTree](avl_tree.md), [RedBlackTree](red_black_tree.md) — for self-balancing trees
- [MaxHeap, MinHeap](heap.md) — for heap-based trees
- [PriorityQueue](priority_queue.md) — for prioritized access