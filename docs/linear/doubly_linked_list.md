# DoublyLinkedList

A Python implementation of a classic doubly linked list with a rich, Pythonic API.  
Supports efficient append, prepend, and a variety of list-like operations, including bidirectional iteration.

---

## Overview

`DoublyLinkedList` is a linear data structure consisting of nodes, each containing a value and references to both the next and previous nodes.  
It is designed for use cases where efficient sequential insert/remove operations and bidirectional traversal are needed.

- **Data type:** Any Python object
- **Efficient operations:** O(1) append, prepend, pop (from both ends); O(n) insert, remove, find, and index-based access
- **Features:** Forward and reverse iteration, rich comparison, list-style indexing, copying, reversing, and more

---

## API Reference

### Constructor

```python
DoublyLinkedList(iterable: Optional[Iterable[Any]] = None)
```
Create an empty list or initialize from any iterable.

#### Example
```python
lst = DoublyLinkedList([1, 2, 3])
print(lst)  # DoublyLinkedList([1, 2, 3])
```

---

### Core Methods

#### `append(data: Any) -> None`
Add an element to the end. **O(1)**

#### Example
```python
lst.append(4)  # DoublyLinkedList([1, 2, 3, 4])
```

---

#### `prepend(data: Any) -> None`
Add an element to the beginning. **O(1)**

#### Example
```python
lst.prepend(0)  # DoublyLinkedList([0, 1, 2, 3, 4])
```

---

#### `insert(index: int, data: Any) -> None`
Insert `data` at position `index`. **O(n)**
- Raises `IndexError` if out of range.
- Supports negative indices.

#### Example
```python
lst.insert(2, 'a')  # DoublyLinkedList([0, 1, 'a', 2, 3, 4])
```

---

#### `pop(index: int = -1) -> Any`
Remove and return element at `index` (default: last). **O(1) for ends, O(n) by index**
- Raises `IndexError` if empty or out of range.
- Supports negative indices.

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

#### `copy() -> DoublyLinkedList`
Return a shallow copy. **O(n)**

#### Example
```python
lst2 = lst.copy()
```

---

#### `reverse() -> None`
Reverse the list in place. **O(n)**
- Reverses links; head and tail are updated.

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

#### `from_iterable(iterable: Iterable[Any]) -> DoublyLinkedList`
Create a list from iterable. **O(n)**

#### Example
```python
lst = DoublyLinkedList.from_iterable(range(10))
```

---

### Pythonic Features

#### `__len__() -> int`
Return number of elements.

#### `__iter__()`
Return iterator over elements (forward).

#### `__reversed__()`
Return iterator over elements (backward).

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

| Method      | Args                            | Returns              | Time Complexity | Notes                |
|:------------|:-------------------------------|:---------------------|:---------------|:---------------------|
| `append`    | `data: Any`                     | `None`               | O(1)           |                      |
| `prepend`   | `data: Any`                     | `None`               | O(1)           |                      |
| `insert`    | `index: int, data: Any`         | `None`               | O(n)           | At index, neg. idx   |
| `pop`       | `index: int = -1`               | `Any`                | O(1)/O(n)      | Ends: O(1), index: O(n) |
| `remove`    | `value: Any`                    | `None`               | O(n)           | By value             |
| `get`       | `index: int`                    | `Any`                | O(n)           | By index, neg. idx   |
| `find`      | `value: Any`                    | `int`                | O(n)           | By value             |
| `clear`     | —                               | `None`               | O(1)           |                      |
| `copy`      | —                               | `DoublyLinkedList`   | O(n)           |                      |
| `reverse`   | —                               | `None`               | O(n)           | In-place             |
| `extend`    | `iterable: Iterable[Any]`       | `None`               | O(n)           |                      |
| `to_list`   | —                               | `list[Any]`          | O(n)           |                      |
| `count`     | `value: Any`                    | `int`                | O(n)           |                      |
| `is_empty`  | —                               | `bool`               | O(1)           |                      |

---

## Example Usage

```python
from pystructures.linear import DoublyLinkedList

lst = DoublyLinkedList([1, 2, 3])
lst.append(4)
lst.prepend(0)
print(lst)  # DoublyLinkedList([0, 1, 2, 3, 4])

print(lst.pop())      # 4
print(lst.get(0))     # 0

lst.reverse()
print(lst)            # DoublyLinkedList([4, 3, 2, 1, 0])

lst.remove(1)
print(lst)            # DoublyLinkedList([4, 3, 2, 0])

lst2 = lst.copy()
print(lst2 == lst)    # True

print(lst.to_list())  # [4, 3, 2, 0]

# Bidirectional iteration
for x in lst:
    print(x)          # Forward: 4 3 2 0
for x in reversed(lst):
    print(x)          # Reverse: 0 2 3 4
```

---

## Notes

- All elements are stored as-is (supports any Python object).
- Negative indices supported for access and assignment.
- Implements full iterator and container protocols.
- Supports reverse iteration (`__reversed__`) for easy backward traversal.
- For bulk operations, prefer `extend` or `from_iterable`.
- For advanced usage, see [source code](../../pystructures/linear/doubly_linked_list.py).

---

## See Also

- [SinglyLinkedList](singly_linked_list.md) — for unidirectional traversal
- [Stack](stack.md), [Queue](queue.md) — for LIFO/FIFO variants