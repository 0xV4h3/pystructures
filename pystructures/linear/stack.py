from typing import Any, Optional, Iterator, Iterable
from copy import deepcopy

class Stack:
    """
    Stack: classic LIFO container with a rich Pythonic API.
    - O(1) push/pop/peek operations.
    - Iterator, comparison, copy, bulk operations, and utility methods.
    - Stores any Python object.
    """

    class _Node:
        __slots__ = ('data', 'next')
        def __init__(self, data: Any, next: Optional['Stack._Node'] = None):
            self.data = data
            self.next = next

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize an empty stack or fill from iterable (bottom to top).
        The last element of iterable becomes the top of the stack (LIFO).
        """
        self._top: Optional[Stack._Node] = None
        self._size: int = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, data: Any) -> None:
        """
        Add data to the top of the stack. O(1).
        """
        self._top = self._Node(data, self._top)
        self._size += 1

    def pop(self) -> Any:
        """
        Remove and return the top element. Raises IndexError if empty. O(1).
        """
        if self._top is None:
            raise IndexError("Pop from empty stack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.data

    def peek(self) -> Any:
        """
        Return the top element without removing. Raises IndexError if empty. O(1).
        """
        if self._top is None:
            raise IndexError("Peek from empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty. O(1).
        """
        return self._size == 0

    def clear(self) -> None:
        """
        Remove all elements from the stack. O(1).
        """
        self._top = None
        self._size = 0

    def copy(self) -> 'Stack':
        """
        Return a shallow copy of the stack. O(n).
        """
        items = list(self)
        return Stack(reversed(items))

    def __copy__(self) -> 'Stack':
        return self.copy()

    def __deepcopy__(self, memo) -> 'Stack':
        items = [deepcopy(x, memo) for x in self]
        return Stack(reversed(items))

    def __len__(self) -> int:
        """
        Return the number of elements in the stack. O(1).
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterator over elements from top to bottom (LIFO order). O(n).
        """
        node = self._top
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        String representation. O(n).
        """
        return f"Stack([{', '.join(repr(x) for x in self)}])"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        """
        Compare stacks element-wise. O(n).
        """
        if not isinstance(other, Stack):
            return False
        return list(self) == list(other)

    def __contains__(self, value: Any) -> bool:
        """
        Return True if value exists in stack. O(n).
        """
        return self.contains(value)

    def contains(self, value: Any) -> bool:
        """
        Return True if value exists in stack. O(n).
        """
        node = self._top
        while node:
            if node.data == value:
                return True
            node = node.next
        return False

    def count(self, value: Any) -> int:
        """
        Count occurrences of value. O(n).
        """
        cnt = 0
        node = self._top
        while node:
            if node.data == value:
                cnt += 1
            node = node.next
        return cnt

    def to_list(self) -> list[Any]:
        """
        Convert stack to Python list (top to bottom). O(n).
        """
        return list(self)

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Push all elements from iterable (first in iterable ends up at bottom). O(n).
        The last element of iterable becomes the top of the stack (LIFO).
        """
        for item in iterable:
            self.push(item)

    @classmethod
    def from_iterable(cls, iterable: Iterable[Any]) -> 'Stack':
        """
        Create a stack from iterable. O(n).
        """
        return cls(iterable)

    def get(self, index: int) -> Any:
        """
        Return element by index (0 = top). O(n).
        Raises IndexError if out of range.
        """
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        node = self._top
        for _ in range(index):
            node = node.next  # type: ignore
        return node.data  # type: ignore

    def find(self, value: Any) -> int:
        """
        Return index of first occurrence of value (top=0), or -1 if not found. O(n).
        """
        idx = 0
        node = self._top
        while node:
            if node.data == value:
                return idx
            node = node.next
            idx += 1
        return -1

    def __getitem__(self, index: int) -> Any:
        """
        Indexing: stack[index], 0 = top. O(n).
        """
        return self.get(index)