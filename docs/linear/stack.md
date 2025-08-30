# Stack

A Python implementation of a classic **LIFO (Last-In, First-Out) stack** with a strict, Pythonic API.  
Supports efficient push/pop/peek operations, copying, bulk operations, and more.

---

## Overview

`Stack` is a linear data structure in which the last element added is the first to be removed.  
It is ideal for scenarios requiring LIFO access—such as undo mechanisms, parsing, backtracking, and more.

- **Data type:** Any Python object
- **Efficient operations:** O(1) push, pop, peek, clear
- **Features:** Comparison, copying, bulk/batch operations, element search

---

## API Reference

### Constructor

```python
Stack(iterable: Optional[Iterable[Any]] = None)
```
Create an empty stack or initialize from any iterable (last element will be on top).

#### Example
```python
stk = Stack([1, 2, 3])
print(stk)  # Stack([3, 2, 1])  # Top is 3
```

---

### Core Methods

#### `push(data: Any) -> None`
Add an element to the **top** of the stack. **O(1)**

#### Example
```python
stk.push(4)  # Stack([4, 3, 2, 1])
```

---

#### `pop() -> Any`
Remove and return the **top** element. **O(1)**
- Raises `IndexError` if empty.

#### Example
```python
top = stk.pop()  # Returns 4, Stack is now Stack([3, 2, 1])
```

---

#### `peek() -> Any`
Return the **top** element without removing it. **O(1)**
- Raises `IndexError` if empty.

#### Example
```python
stk.peek()  # Returns 3
```

---

#### `is_empty() -> bool`
Check if the stack is empty. **O(1)**
```python
stk.is_empty()  # True/False
```

---

#### `clear() -> None`
Remove all elements. **O(1)**
```python
stk.clear()
```

---

#### `copy() -> Stack`
Return a shallow copy (LIFO order preserved). **O(n)**
```python
stk2 = stk.copy()
```

---

#### `extend(iterable: Iterable[Any]) -> None`
Push all elements from `iterable` (last element becomes the new top). **O(n)**
```python
stk.extend([5, 6])  # 6 at top, 5 below
```

---

#### `to_list() -> list[Any]`
Convert to built-in Python list (top to bottom). **O(n)**
```python
py_list = stk.to_list()  # [top, ... bottom]
```

---

#### `from_iterable(iterable: Iterable[Any]) -> Stack`
Create a stack from iterable. **O(n)**
```python
stk = Stack.from_iterable(range(3))  # Stack([2, 1, 0])
```

---

### Search & Utility

#### `count(value: Any) -> int`
Count occurrences of value. **O(n)**
```python
stk.count(3)
```

---

#### `contains(value: Any) -> bool`
Check if value exists in stack. **O(n)**
```python
stk.contains(2)  # True/False
```
Supports `value in stk`.

---

### Pythonic Features

#### `__len__() -> int`
Return number of elements.

#### `__str__()`, `__repr__()`
String representations.

#### `__eq__(other: object) -> bool`
Element-wise comparison.

---

## Method Overview

| Method      | Args                      | Returns      | Time Complexity   | Notes          |
|:------------|:--------------------------|:-------------|:------------------|:---------------|
| `push`      | `data: Any`               | `None`       | O(1)              | Top            |
| `pop`       | —                         | `Any`        | O(1)              | Top            |
| `peek`      | —                         | `Any`        | O(1)              | Top            |
| `is_empty`  | —                         | `bool`       | O(1)              |                |
| `clear`     | —                         | `None`       | O(1)              |                |
| `copy`      | —                         | `Stack`      | O(n)              | LIFO order     |
| `extend`    | `iterable: Iterable[Any]` | `None`       | O(n)              | Bulk push      |
| `to_list`   | —                         | `list[Any]`  | O(n)              | Top → bottom   |
| `count`     | `value: Any`              | `int`        | O(n)              |                |
| `contains`  | `value: Any`              | `bool`       | O(n)              |                |

---

## Example Usage

```python
from pystructures.linear import Stack

stk = Stack([1, 2, 3])
print(stk)         # Stack([3, 2, 1])
stk.push(4)
print(stk.peek())  # 4
print(stk.pop())   # 4
print(stk.to_list())   # [3, 2, 1]
print(3 in stk)    # True
stk.clear()
print(stk.is_empty())  # True
stk.extend([5, 6])
print(stk)         # Stack([6, 5])
stk2 = stk.copy()
print(stk2 == stk) # True
```

---

## Notes

- All elements are stored as-is (supports any Python object).
- Implements full container protocol (`__len__`, `__contains__`, `__eq__`, etc.).
- Bulk operations (`extend`, `from_iterable`) preserve LIFO order (last in iterable becomes top).
- For advanced usage, see [source code](../../pystructures/linear/stack.py).

---

## See Also

- [SinglyLinkedList](singly_linked_list.md) — for sequential access
- [DoublyLinkedList](doubly_linked_list.md) — for bidirectional traversal
- [Queue](queue.md) — for FIFO variants