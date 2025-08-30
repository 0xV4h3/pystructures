# Queue

A Python implementation of a classic **FIFO (First-In, First-Out) queue** with a strict, Pythonic API.  
Supports efficient enqueue, dequeue, front/rear access, copying, bulk operations, and more.

---

## Overview

`Queue` is a linear data structure in which the first element added is the first to be removed.  
It is ideal for scenarios requiring FIFO access—such as job scheduling, buffering, breadth-first search, and more.

- **Data type:** Any Python object
- **Efficient operations:** O(1) enqueue, dequeue, front, rear, clear
- **Features:** Comparison, copying, bulk/batch operations, element search

---

## API Reference

### Constructor

```python
Queue(iterable: Optional[Iterable[Any]] = None)
```
Create an empty queue or initialize from any iterable (first element will be at the front).

#### Example
```python
q = Queue([1, 2, 3])
print(q)  # Queue([1, 2, 3])  # Front is 1, rear is 3
```

---

### Core Methods

#### `enqueue(data: Any) -> None`
Add an element to the **rear** of the queue. **O(1)**

#### Example
```python
q.enqueue(4)  # Queue([1, 2, 3, 4])
```

---

#### `dequeue() -> Any`
Remove and return the **front** element. **O(1)**
- Raises `IndexError` if empty.

#### Example
```python
front = q.dequeue()  # Returns 1, Queue is now Queue([2, 3, 4])
```

---

#### `front() -> Any`
Return the **front** element without removing it. **O(1)**
- Raises `IndexError` if empty.

#### Example
```python
q.front()  # Returns 2
```

---

#### `rear() -> Any`
Return the **rear** element without removing it. **O(1)**
- Raises `IndexError` if empty.

#### Example
```python
q.rear()  # Returns 4
```

---

#### `is_empty() -> bool`
Check if the queue is empty. **O(1)**
```python
q.is_empty()  # True/False
```

---

#### `clear() -> None`
Remove all elements. **O(1)**
```python
q.clear()
```

---

#### `copy() -> Queue`
Return a shallow copy (FIFO order preserved). **O(n)**
```python
q2 = q.copy()
```

---

#### `extend(iterable: Iterable[Any]) -> None`
Enqueue all elements from `iterable` (first in iterable ends up at rear). **O(n)**
```python
q.extend([5, 6])  # 5 at rear, then 6
```

---

#### `to_list() -> list[Any]`
Convert to built-in Python list (front to rear). **O(n)**
```python
py_list = q.to_list()  # [front, ..., rear]
```

---

#### `from_iterable(iterable: Iterable[Any]) -> Queue`
Create a queue from iterable. **O(n)**
```python
q = Queue.from_iterable(range(3))  # Queue([0, 1, 2])
```

---

### Search & Utility

#### `count(value: Any) -> int`
Count occurrences of value. **O(n)**
```python
q.count(3)
```

---

#### `contains(value: Any) -> bool`
Check if value exists in queue. **O(n)**
```python
q.contains(2)  # True/False
```
Supports `value in q`.

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
| `enqueue`   | `data: Any`               | `None`       | O(1)              | Rear           |
| `dequeue`   | —                         | `Any`        | O(1)              | Front          |
| `front`     | —                         | `Any`        | O(1)              | Front          |
| `rear`      | —                         | `Any`        | O(1)              | Rear           |
| `is_empty`  | —                         | `bool`       | O(1)              |                |
| `clear`     | —                         | `None`       | O(1)              |                |
| `copy`      | —                         | `Queue`      | O(n)              | FIFO order     |
| `extend`    | `iterable: Iterable[Any]` | `None`       | O(n)              | Bulk enqueue   |
| `to_list`   | —                         | `list[Any]`  | O(n)              | Front → rear   |
| `count`     | `value: Any`              | `int`        | O(n)              |                |
| `contains`  | `value: Any`              | `bool`       | O(n)              |                |

---

## Example Usage

```python
from pystructures.linear import Queue

q = Queue([1, 2, 3])
print(q)          # Queue([1, 2, 3])
q.enqueue(4)
print(q.rear())   # 4
print(q.dequeue())# 1
print(q.front())  # 2
print(q.to_list())# [2, 3, 4]
print(3 in q)     # True
q.clear()
print(q.is_empty())  # True
q.extend([5, 6])
print(q)          # Queue([5, 6])
q2 = q.copy()
print(q2 == q)    # True
```

---

## Notes

- All elements are stored as-is (supports any Python object).
- Implements full container protocol (`__len__`, `__contains__`, `__eq__`, etc.).
- Bulk operations (`extend`, `from_iterable`) preserve FIFO order (first in iterable becomes front).
- For advanced usage, see [source code](../../pystructures/linear/queue.py).

---

## See Also

- [SinglyLinkedList](singly_linked_list.md) — for sequential access
- [DoublyLinkedList](doubly_linked_list.md) — for bidirectional traversal
- [Stack](stack.md) — for LIFO variants