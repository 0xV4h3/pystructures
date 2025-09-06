from typing import Any, Iterable, Iterator, Optional, TypeVar, Type
from abc import ABC, abstractmethod
from copy import deepcopy

__all__ = ["MaxHeap", "MinHeap"]

T = TypeVar("T", bound="_Heap")

class _Heap(ABC):
    """
    Internal base class for MaxHeap/MinHeap.
    Implements core heap operations with a Pythonic API.
    Not for direct use.
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize an empty heap, or bulk-load from iterable.
        """
        self._data: list[Any] = []
        if iterable is not None:
            self.heapify(iterable)

    def push(self, item: Any) -> None:
        """
        Add a new item to the heap. O(log n).
        """
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Any:
        """
        Remove and return the root element (max or min).
        Raises IndexError if heap is empty. O(log n).
        """
        if not self._data:
            raise IndexError("Pop from empty heap")
        root = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return root

    def peek(self) -> Any:
        """
        Return the root element without removing.
        Raises IndexError if heap is empty. O(1).
        """
        if not self._data:
            raise IndexError("Peek from empty heap")
        return self._data[0]

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Add all items from iterable to heap, one by one. O(k log n).
        """
        for item in iterable:
            self.push(item)

    def heapify(self, iterable: Iterable[Any]) -> None:
        """
        Bulk-load heap from iterable, efficiently. O(n).
        Replaces current contents.
        """
        self._data = list(iterable)
        n = len(self._data)
        for i in reversed(range(n // 2)):
            self._sift_down(i)

    @classmethod
    def from_iterable(cls: Type[T], iterable: Iterable[Any]) -> T:
        """
        Create a new heap instance from iterable. O(n).
        """
        return cls(iterable)

    def clear(self) -> None:
        """
        Remove all elements from heap. O(1).
        """
        self._data.clear()

    def copy(self) -> "T":
        """
        Return a shallow copy of the heap. O(n).
        """
        return self.__class__(self._data)

    def __copy__(self: T) -> T:
        """Support for copy.copy(). O(n)."""
        return self.copy()

    def __deepcopy__(self: T, memo) -> T:
        """Support for copy.deepcopy(). O(n)."""
        copied_data = deepcopy(self._data, memo)
        return self.__class__(copied_data)

    def to_list(self) -> list[Any]:
        """
        Return list of all elements (internal order). O(n).
        """
        return list(self._data)

    def __len__(self) -> int:
        """
        Return number of elements in heap. O(1).
        """
        return len(self._data)

    def is_empty(self) -> bool:
        """
        Return True if heap is empty. O(1).
        """
        return not self._data

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over elements (internal order, not sorted). O(n).
        """
        return iter(self._data)

    def __contains__(self, item: Any) -> bool:
        """
        Return True if item is in heap. O(n).
        """
        return item in self._data

    def count(self, item: Any) -> int:
        """
        Return number of occurrences of item. O(n).
        """
        return self._data.count(item)

    def __eq__(self, other: object) -> bool:
        """
        Compare heaps by their contents (internal order). O(n).
        """
        if not isinstance(other, _Heap):
            return False
        return self._data == other._data

    def __str__(self) -> str:
        """
        String representation of the heap (internal order). O(n)
        """
        return f"{self.__class__.__name__}([{', '.join(repr(x) for x in self._data)}])"

    def __repr__(self) -> str:
        """
        Debug representation of the heap. O(n)
        """
        return str(self)

    @staticmethod
    def _parent(index: int) -> int:
        """
        Return parent index for given index.
        """
        return (index - 1) // 2

    @staticmethod
    def _left(index: int) -> int:
        """
        Return left child index for given index.
        """
        return 2 * index + 1

    @staticmethod
    def _right(index: int) -> int:
        """
        Return right child index for given index.
        """
        return 2 * index + 2

    def _sift_up(self, index: int) -> None:
        """
        Restore heap property up from index.
        """
        while index > 0:
            parent = self._parent(index)
            if self._compare(self._data[index], self._data[parent]):
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                index = parent
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Restore heap property down from index.
        """
        n = len(self._data)
        while True:
            left = self._left(index)
            right = self._right(index)
            best = index
            if left < n and self._compare(self._data[left], self._data[best]):
                best = left
            if right < n and self._compare(self._data[right], self._data[best]):
                best = right
            if best == index:
                break
            self._data[index], self._data[best] = self._data[best], self._data[index]
            index = best

    @abstractmethod
    def _compare(self, a: Any, b: Any) -> bool:
        """
        Compare two elements for heap property.
        Must be implemented in subclass.
        """
        pass

class MaxHeap(_Heap):
    """
    MaxHeap: root is always the largest element.
    """
    def _compare(self, a: Any, b: Any) -> bool:
        return a > b

class MinHeap(_Heap):
    """
    MinHeap: root is always the smallest element.
    """
    def _compare(self, a: Any, b: Any) -> bool:
        return a < b