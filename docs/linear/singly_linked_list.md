# SinglyLinkedList

A Python implementation of a classic singly linked list with a rich, Pythonic API.  
Supports efficient append, prepend, and a variety of list-like operations.

---

## Overview

`SinglyLinkedList` is a linear data structure consisting of nodes, each containing a value and a reference to the next node.  
It is designed for use cases where efficient sequential insert/remove operations are needed, and direct indexed access is less frequent.

- **Data type:** Any Python object
- **Efficient operations:** O(1) append, prepend; O(n) insert, remove, pop, find, and index-based access
- **Features:** Iteration, rich comparison, list-style indexing, copying, reversing, and more

---

## API Reference

### Constructor

```python
SinglyLinkedList(iterable: Optional[Iterable[Any]] = None)
```
Create an empty list or initialize from any iterable.

#### Example
```python
lst = SinglyLinkedList([1, 2, 3])
print(lst)  # SinglyLinkedList([1, 2, 3])
```

---

### Core Methods

#### `append(data: Any) -> None`
Add an element to the end. **O(1)**

#### Example
```python
lst.append(4)  # SinglyLinkedList([1, 2, 3, 4])
```

---

#### `prepend(data: Any) -> None`
Add an element to the beginning. **O(1)**

#### Example
```python
lst.prepend(0)  # SinglyLinkedList([0, 1, 2, 3, 4])
```

---

#### `insert(index: int, data: Any) -> None`
Insert `data` at position `index`. **O(n)**
- Raises `IndexError` if out of range.

#### Example
```python
lst.insert(2, 'a')  # SinglyLinkedList([0, 1, 'a', 2, 3, 4])
```

---

#### `pop(index: int = -1) -> Any`
Remove and return element at `index` (default: last). **O(n)**
- Raises `IndexError` if empty or out of range.

#### Example
```python
last = lst.pop()       # Removes and returns last element
first = lst.pop(0)     # Removes and returns first element
```

---

#### `remove(value: Any) -> None`
Remove first occurrence of `value`. **O(n)**
- Raises `ValueError` if not found.

#### Example
```python
lst.remove('a')  # Remove 'a' from the list
```

---

#### `get(index: int) -> Any`
Return value at `index`. **O(n)**
- Supports negative indices.
- Raises `IndexError` if out of range.

#### Example
```python
val = lst.get(2)     # Get value at index 2
val = lst.get(-1)    # Get last value
```

---

#### `find(value: Any) -> int`
Return index of first occurrence, or -1 if not found. **O(n)**

#### Example
```python
idx = lst.find(2)  # Index of value 2
```

---

#### `clear() -> None`
Remove all elements. **O(1)**

#### Example
```python
lst.clear()
```

---

#### `copy() -> SinglyLinkedList`
Return a shallow copy. **O(n)**

#### Example
```python
lst2 = lst.copy()
```

---

#### `reverse() -> None`
Reverse the list in place. **O(n)**

#### Example
```python
lst.reverse()
```

---

#### `extend(iterable: Iterable[Any]) -> None`
Append all elements from `iterable`. **O(n)**

#### Example
```python
lst.extend([5, 6])
```

---

#### `to_list() -> list[Any]`
Convert to built-in Python list. **O(n)**

#### Example
```python
py_list = lst.to_list()
```

---

#### `from_iterable(iterable: Iterable[Any]) -> SinglyLinkedList`
Create a list from iterable. **O(n)**

#### Example
```python
lst = SinglyLinkedList.from_iterable(range(10))
```

---

### Pythonic Features

#### `__len__() -> int`
Return number of elements.

#### `__iter__()`
Return iterator over elements.

#### `__str__()`, `__repr__()`
String representations.

#### `__getitem__(index: int) -> Any`
Indexing: `lst[index]`.

#### `__setitem__(index: int, value: Any) -> None`
Assignment: `lst[index] = value`.

#### `__eq__(other: object) -> bool`
Element-wise comparison.

---

### Utility Methods

#### `contains(value: Any) -> bool`
Check if value exists (`value in lst`).

#### `count(value: Any) -> int`
Count occurrences of value.

#### `is_empty() -> bool`
Check if list is empty.

---

## Method Overview

| Method      | Args                      | Returns      | Time Complexity | Notes    |
|:------------|:--------------------------|:-------------|:---------------|:---------|
| `append`    | `data: Any`               | `None`       | O(1)           |          |
| `prepend`   | `data: Any`               | `None`       | O(1)           |          |
| `insert`    | `index: int, data: Any`   | `None`       | O(n)           | At index |
| `pop`       | `index: int = -1`         | `Any`        | O(n)           | By index |
| `remove`    | `value: Any`              | `None`       | O(n)           | By value |
| `get`       | `index: int`              | `Any`        | O(n)           | By index |
| `find`      | `value: Any`              | `int`        | O(n)           | By value |
| `clear`     | —                         | `None`       | O(1)           |          |
| `copy`      | —                         | `SinglyLinkedList` | O(n)     |          |
| `reverse`   | —                         | `None`       | O(n)           | In-place |
| `extend`    | `iterable: Iterable[Any]` | `None`       | O(n)           |          |
| `to_list`   | —                         | `list[Any]`  | O(n)           |          |
| `count`     | `value: Any`              | `int`        | O(n)           |          |
| `is_empty`  | —                         | `bool`       | O(1)           |          |

---

## Example Usage

```python
from pystructures.linear import SinglyLinkedList

lst = SinglyLinkedList([1, 2, 3])
lst.append(4)
lst.prepend(0)
print(lst)  # SinglyLinkedList([0, 1, 2, 3, 4])

print(lst.pop())      # 4
print(lst.get(0))     # 0

lst.reverse()
print(lst)            # SinglyLinkedList([3, 2, 1, 0])

lst.remove(1)
print(lst)            # SinglyLinkedList([3, 2, 0])

lst2 = lst.copy()
print(lst2 == lst)    # True

print(lst.to_list())  # [3, 2, 0]
```

---

## Notes

- All elements are stored as-is (supports any Python object).
- Negative indices supported for access and assignment.
- Implements full iterator and container protocols.
- For bulk operations, prefer `extend` or `from_iterable`.
- For advanced usage, see [source code](../../pystructures/linear/singly_linked_list.py).

---

## See Also

- [DoublyLinkedList](doubly_linked_list.md) — for bidirectional traversal
- [Stack](stack.md), [Queue](queue.md) — for LIFO/FIFO variants