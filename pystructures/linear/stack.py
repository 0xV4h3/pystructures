from typing import Any, Optional, Iterable, TypeVar, Type
from copy import deepcopy

T = TypeVar("T", bound="Stack")

class Stack:
    """
    Stack: classic LIFO container.
    - O(1) push/pop/peek operations.
    - No iterator or index-based access.
    - Comparison, copy, bulk operations, and utility methods.
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
        Add data to the top of the stack.
        O(1)
        """
        self._top = self._Node(data, self._top)
        self._size += 1

    def pop(self) -> Any:
        """
        Remove and return the top element. Raises IndexError if empty.
        O(1)
        """
        if self._top is None:
            raise IndexError("Pop from empty stack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.data

    def peek(self) -> Any:
        """
        Return the top element without removing. Raises IndexError if empty.
        O(1)
        """
        if self._top is None:
            raise IndexError("Peek from empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        """
        Return True if the stack is empty.
        O(1)
        """
        return self._size == 0

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        O(1)
        """
        self._top = None
        self._size = 0

    def copy(self) -> T:
        """
        Return a shallow copy of the stack.
        O(n)
        """
        items = []
        node = self._top
        while node:
            items.append(node.data)
            node = node.next  # type: ignore
        return Stack(reversed(items))

    def __copy__(self) -> T:
        """
        Support for copy.copy().
        O(n)
        """
        return self.copy()

    def __deepcopy__(self, memo) -> T:
        """
        Support for copy.deepcopy().
        O(n)
        """
        items = []
        node = self._top
        while node:
            items.append(deepcopy(node.data, memo))
            node = node.next  # type: ignore
        return Stack(reversed(items))

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Push all elements from iterable.
        The last element of iterable becomes the top of the stack (LIFO).
        O(n)
        """
        for item in iterable:
            self.push(item)

    @classmethod
    def from_iterable(cls: Type[T], iterable: Iterable[Any]) -> T:
        """
        Create a stack from iterable.
        O(n)
        """
        return cls(iterable)

    def to_list(self) -> list[Any]:
        """
        Convert stack to Python list (top to bottom).
        O(n)
        """
        items = []
        node = self._top
        while node:
            items.append(node.data)
            node = node.next  # type: ignore
        return items

    def contains(self, value: Any) -> bool:
        """
        Return True if value exists in stack.
        O(n)
        """
        node = self._top
        while node:
            if node.data == value:
                return True
            node = node.next  # type: ignore
        return False

    def count(self, value: Any) -> int:
        """
        Count occurrences of value.
        O(n)
        """
        cnt = 0
        node = self._top
        while node:
            if node.data == value:
                cnt += 1
            node = node.next  # type: ignore
        return cnt

    def __contains__(self, value: Any) -> bool:
        """
        Return True if value exists in stack.
        O(n)
        """
        return self.contains(value)

    def __len__(self) -> int:
        """
        Return the number of elements in the stack.
        O(1)
        """
        return self._size

    def __str__(self) -> str:
        """
        String representation.
        O(n)
        """
        items = []
        node = self._top
        while node:
            items.append(repr(node.data))
            node = node.next  # type: ignore
        return f"Stack([{', '.join(items)}])"

    def __repr__(self) -> str:
        """
        Representation for debugging.
        O(n)
        """
        return str(self)

    def __eq__(self, other: object) -> bool:
        """
        Compare stacks element-wise.
        O(n)
        """
        if not isinstance(other, Stack):
            return False
        a, b = self._top, other._top  # type: ignore
        while a and b:
            if a.data != b.data:
                return False
            a = a.next  # type: ignore
            b = b.next  # type: ignore
        return a is None and b is None