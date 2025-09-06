# PriorityQueue

A Pythonic implementation of a stable, feature-rich priority queue built atop **MinHeap**/**MaxHeap**.  
Supports efficient prioritized insertion/removal, custom key functions, FIFO stability, bulk operations, copying, and more.

---

## Overview

`PriorityQueue` is a classic data structure that stores elements with associated *priorities*.  
It always removes or peeks the element with the highest or lowest priority, and is stable (FIFO) for duplicate priorities.

- **Stable:** Maintains insertion order for elements with equal priority.
- **Flexible:** Accepts any mutually comparable priority type (`int`, `float`, `str`, etc.), and arbitrary Python objects as values.
- **Custom key:** Supports extracting priority using a user-defined function.
- **Efficient:** O(log n) insert/remove, O(1) peek; O(n) for bulk operations.
- **Features:** Bulk/batch extension, copying, deep copying, iteration, comparison, count/search, conversion to list.

---

## API Reference

### Constructor

```python
PriorityQueue(
    iterable: Optional[Iterable[Any]] = None,
    ascending: bool = True,
    key: Optional[Callable[[Any], Any]] = None
)
```
Create an empty queue or initialize from iterable (each item may be a value or `(priority, value)` pair). **O(n) if iterable given, O(1) otherwise**

#### Example
```python
from pystructures.nonlinear import PriorityQueue

pq = PriorityQueue([(3, "low"), (1, "urgent")])
pq2 = PriorityQueue(["a", "bb", "ccc"], key=len)
pq3 = PriorityQueue([("high", "A"), ("low", "B")], ascending=False)
```

---

### Core Methods

#### `push(value: Any, priority: Optional[Any] = None) -> None`
Add a value with a given priority. If priority is omitted, uses `key(value)`. **O(log n)**

#### Example
```python
pq.push("task", priority=5)
pq.push("auto", priority=None)  # Uses key if provided
```

---

#### `pop() -> Any`
Remove and return the value with highest/lowest priority. Raises `IndexError` if empty. **O(log n)**

#### Example
```python
item = pq.pop()
```

---

#### `popitem() -> tuple[Any, Any]`
Remove and return `(priority, value)` pair. Raises `IndexError` if empty. **O(log n)**

#### Example
```python
prio, item = pq.popitem()
```

---

#### `peek() -> Any`
Return the value with highest/lowest priority without removing. Raises `IndexError` if empty. **O(1)**

#### Example
```python
pq.peek()
```

---

#### `peekitem() -> tuple[Any, Any]`
Return `(priority, value)` pair without removing. Raises `IndexError` if empty. **O(1)**

#### Example
```python
pq.peekitem()
```

---

#### `clear() -> None`
Remove all elements. **O(1)**

#### Example
```python
pq.clear()
```

---

#### `extend(iterable: Iterable[Any]) -> None`
Add all elements from an iterable (each item may be a value or `(priority, value)`). **O(k log n)** for k elements

#### Example
```python
pq.extend([(2, "A"), (4, "B")])
pq.extend(["C", "D"])  # Uses key if provided
```

---

#### `to_list() -> list[Any]`
Convert queue to a list of values (internal heap order). **O(n)**

#### Example
```python
lst = pq.to_list()
```

---

#### `to_pair_list() -> list[tuple[Any, Any]]`
Convert to a list of `(priority, value)` pairs (internal heap order). **O(n)**

#### Example
```python
pairs = pq.to_pair_list()
```

---

#### `copy() -> PriorityQueue`
Return a shallow copy. **O(n)**

#### Example
```python
pq2 = pq.copy()
```

---

#### `__copy__() -> PriorityQueue`
Support for `copy.copy()`. **O(n)**

---

#### `__deepcopy__(memo) -> PriorityQueue`
Support for `copy.deepcopy()`. **O(n)**

---

#### `from_iterable(iterable: Iterable[Any], ascending: bool = True, key: Optional[Callable[[Any], Any]] = None) -> PriorityQueue`
Class method to create a queue from iterable (bulk load). **O(n)**

#### Example
```python
pq = PriorityQueue.from_iterable([(3, "low"), (1, "urgent")])
```

---

#### `count(value: Any) -> int`
Count occurrences of a value. **O(n)**

#### Example
```python
pq.count("low")
```

---

#### `__contains__(value: Any) -> bool`
Check if a value exists. **O(n)**

#### Example
```python
"urgent" in pq
```

---

#### `__len__() -> int`
Return number of elements. **O(1)**

---

#### `is_empty() -> bool`
Check if empty. **O(1)**

---

#### `__iter__()`
Iterate over values (internal heap order). **O(n)**

---

#### `__eq__(other: object) -> bool`
Element-wise comparison. **O(n)**

---

#### `__str__()`, `__repr__()`
String representations. **O(n)**

---

## Method Overview

| Method        | Args                               | Returns                | Complexity   | Notes            |
|:------------- |:-----------------------------------|:-----------------------|:-------------|:-----------------|
| `push`        | `value, priority=None`             | `None`                 | O(log n)     |                  |
| `pop`         | —                                 | `Any`                  | O(log n)     | Value            |
| `popitem`     | —                                 | `(priority, value)`    | O(log n)     | Pair             |
| `peek`        | —                                 | `Any`                  | O(1)         | Value            |
| `peekitem`    | —                                 | `(priority, value)`    | O(1)         | Pair             |
| `clear`       | —                                 | `None`                 | O(1)         |                  |
| `extend`      | `iterable`                        | `None`                 | O(k log n)   | Bulk insert      |
| `to_list`     | —                                 | `list[Any]`            | O(n)         | Internal order   |
| `to_pair_list`| —                                 | `list[(priority, value)]`| O(n)       | Internal order   |
| `copy`        | —                                 | `PriorityQueue`        | O(n)         | Shallow copy     |
| `from_iterable`| `iterable, ascending, key`        | `PriorityQueue`        | O(n)         | Bulk build       |
| `count`       | `value`                           | `int`                  | O(n)         |                  |
| `is_empty`    | —                                 | `bool`                 | O(1)         |                  |

---

## Example Usage

```python
from pystructures.nonlinear import PriorityQueue

# With explicit priorities
pq = PriorityQueue([(3, "low"), (1, "urgent")])
pq.push("medium", priority=2)

print(pq.peek())         # "urgent" (lowest priority value)
print(pq.popitem())      # (1, "urgent")
print(pq.to_list())      # ["medium", "low"]

# With custom key
pq2 = PriorityQueue(["aaa", "bb", "c"], key=len)
print(pq2.pop())         # "c" (shortest string)

# Bulk extension
pq.extend([("critical", "A"), ("minor", "B")])
print(len(pq))           # 4
pq.clear()

# Copying
pq3 = pq2.copy()
print(pq3 == pq2)        # True

# From iterable
pq4 = PriorityQueue.from_iterable([(5, "A"), (2, "B")])
print(pq4.peekitem())    # (2, "B")
```

---

## Notes & Edge Cases

- **Stability:** When multiple elements have equal priority, dequeue order is FIFO (first-in, first-out).
- **Priority types:** All priorities must be mutually comparable (e.g., all ints, or all strings). Mixing types (e.g., int and str) will raise `TypeError`.
- **Bulk operations:** Bulk methods (`extend`, `from_iterable`) are efficient for batch loads.
- **Iteration:** Yields values in internal heap order, not sorted by priority.
- For advanced sorting, repeatedly call `pop()` until empty.
- For heap details, see [Heap](heap.md).

---

## See Also

- [Heap](heap.md) — underlying implementation
- [Stack](../linear/stack.md), [Queue](../linear/queue.md)
- [BinaryTree](binary_tree.md), [Trie](trie.md)