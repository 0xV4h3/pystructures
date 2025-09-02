# MaxHeap & MinHeap

A Pythonic implementation of classic binary heap structures: **MaxHeap** and **MinHeap**.  
Both provide efficient O(log n) insert, pop, and O(1) peek operations, along with modern container features and a unified, extensible API.

---

## Overview

**Heap** is a nonlinear hierarchical data structure based on a binary tree, supporting fast access to either the maximum (**MaxHeap**) or minimum (**MinHeap**) element.

- **MaxHeap:** root is always the largest element; uses `a > b` comparison.
- **MinHeap:** root is always the smallest element; uses `a < b` comparison.
- All heap operations and API are the same except for the comparator.
- Elements must be **mutually comparable** (e.g., all ints, or all strings); mixing types will raise `TypeError`.

---

## API Reference

### Constructors

```python
MaxHeap(iterable: Optional[Iterable[Any]] = None)
MinHeap(iterable: Optional[Iterable[Any]] = None)
```
Create an empty heap or initialize from any iterable (bulk heapify).

#### Example
```python
from pystructures.nonlinear import MaxHeap, MinHeap

maxh = MaxHeap([5, 2, 9, 1])  # MaxHeap([9, 5, 2, 1])
minh = MinHeap([5, 2, 9, 1])  # MinHeap([1, 2, 9, 5])
```

---

### Core Methods

#### `push(item: Any) -> None`
Add an item to the heap. **O(log n)**

#### Example
```python
maxh.push(7)  # MaxHeap([9, 7, 2, 1, 5])
minh.push(7)  # MinHeap([1, 2, 7, 9, 5])
```

---

#### `pop() -> Any`
Remove and return the root element (max for MaxHeap, min for MinHeap). **O(log n)**
- Raises `IndexError` if heap is empty.

#### Example
```python
max_val = maxh.pop()  # 9
min_val = minh.pop()  # 1
```

---

#### `peek() -> Any`
Return the root element without removing. **O(1)**
- Raises `IndexError` if heap is empty.

#### Example
```python
maxh.peek()  # 7
minh.peek()  # 2
```

---

#### `extend(iterable: Iterable[Any]) -> None`
Add all items from iterable, preserving heap property. **O(k log n)**

#### Example
```python
maxh.extend([3, 8])
minh.extend([3, 8])
```

---

#### `heapify(iterable: Iterable[Any]) -> None`
Bulk-load heap from iterable, efficiently. **O(n)**
- Replaces current heap contents.

#### Example
```python
maxh.heapify([10, 4, 7])
minh.heapify([10, 4, 7])
```

---

#### `clear() -> None`
Remove all elements. **O(1)**

#### Example
```python
maxh.clear()
minh.clear()
```

---

#### `copy() -> MaxHeap/MinHeap`
Return a shallow copy. **O(n)**

#### Example
```python
maxh2 = maxh.copy()
minh2 = minh.copy()
```

---

#### `to_list() -> list[Any]`
Convert heap to a list (internal order, not sorted). **O(n)**

#### Example
```python
lst = maxh.to_list()
lst = minh.to_list()
```

---

#### `from_iterable(iterable: Iterable[Any]) -> MaxHeap/MinHeap`
Create a heap from iterable. **O(n)**

#### Example
```python
maxh = MaxHeap.from_iterable(range(10))
minh = MinHeap.from_iterable(range(10))
```

---

### Pythonic Features

#### `__len__() -> int`
Return number of elements.

#### `__iter__()`
Return iterator over heap elements (internal order).

#### `__contains__(item: Any) -> bool`
Check if item exists in heap.

#### `count(item: Any) -> int`
Count occurrences of item.

#### `is_empty() -> bool`
Check if heap is empty.

#### `__eq__(other: object) -> bool`
Element-wise comparison.

#### `__str__()`, `__repr__()`
String representations.

---

## Method Overview

| Method      | Args                      | Returns      | Time Complexity   | Notes    |
|:------------|:--------------------------|:-------------|:------------------|:---------|
| `push`      | `item: Any`               | `None`       | O(log n)          |          |
| `pop`       | —                         | `Any`        | O(log n)          | Root element |
| `peek`      | —                         | `Any`        | O(1)              | Root element |
| `extend`    | `iterable: Iterable[Any]` | `None`       | O(k log n)        | Bulk insert |
| `heapify`   | `iterable: Iterable[Any]` | `None`       | O(n)              | Bulk build |
| `clear`     | —                         | `None`       | O(1)              |          |
| `copy`      | —                         | `MaxHeap/MinHeap` | O(n)         | Shallow copy |
| `to_list`   | —                         | `list[Any]`  | O(n)              | Internal order |
| `from_iterable`| `iterable: Iterable[Any]`| `MaxHeap/MinHeap` | O(n)     | Bulk build |
| `count`     | `item: Any`               | `int`        | O(n)              |          |
| `is_empty`  | —                         | `bool`       | O(1)              |          |

---

## Example Usage

```python
from pystructures.nonlinear import MaxHeap, MinHeap

maxh = MaxHeap([2, 8, 5])
minh = MinHeap([2, 8, 5])

maxh.push(10)
minh.push(1)

print(maxh.peek())      # 10
print(minh.peek())      # 1

print(maxh.pop())       # 10
print(minh.pop())       # 1

print(list(maxh))       # [8, 2, 5] (order not guaranteed)
print(list(minh))       # [2, 8, 5]

maxh.extend([1, 7])
minh.extend([1, 7])

maxh2 = maxh.copy()
minh2 = minh.copy()
print(maxh2 == maxh)    # True
print(minh2 == minh)    # True

maxh.clear()
minh.clear()
print(len(maxh))        # 0
print(len(minh))        # 0

maxh3 = MaxHeap.from_iterable([3, 4, 9])
minh3 = MinHeap.from_iterable([3, 4, 9])
print(maxh3.peek())     # 9
print(minh3.peek())     # 3
```

---

## Notes & Edge Cases

- **All elements** must be mutually comparable (`>` for MaxHeap, `<` for MinHeap). Mixing types (e.g. int and str) will raise `TypeError` during insertion or heapify.
- **Bulk methods** (`heapify`, `from_iterable`) are more efficient than repeated `push`.
- **Iteration** yields elements in internal heap order, not sorted order.
- For sorted extraction, repeatedly `pop` until empty.
- Heaps do **not** guarantee full sort order—only the root is guaranteed as min/max.
- For advanced prioritized structures, see [PriorityQueue](priority_queue.md).

---

## See Also

- [PriorityQueue](priority_queue.md) — for advanced priority handling
- [BinaryTree](binary_tree.md), [BinarySearchTree](binary_search_tree.md)
- [Stack](../linear/stack.md), [Queue](../linear/queue.md)