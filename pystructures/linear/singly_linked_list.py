from typing import Any, Optional, Iterator, Iterable
from copy import deepcopy


class SinglyLinkedList:
    """
    SinglyLinkedList implements a classic singly linked list with full Pythonic API.
    - Supports O(1) append/prepend, O(n) insert, remove, pop, find, and index-based access.
    - Iterator protocol (__iter__), rich comparison (__eq__), and list-like methods.
    - Data type: Any.
    """

    class _Node:
        __slots__ = ('data', 'next')

        def __init__(self, data: Any, next: Optional['SinglyLinkedList._Node'] = None):
            self.data = data
            self.next = next

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize an empty list or fill from iterable.
        """
        self._head: Optional[SinglyLinkedList._Node] = None
        self._tail: Optional[SinglyLinkedList._Node] = None
        self._size: int = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, data: Any) -> None:
        """
        Add data to the end of the list. O(1).
        """
        node = self._Node(data)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            assert self._tail is not None
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """
        Add data to the beginning of the list. O(1).
        """
        node = self._Node(data, self._head)
        self._head = node
        if self._size == 0:
            self._tail = node
        self._size += 1

    def insert(self, index: int, data: Any) -> None:
        """
        Insert data at given index. O(n).
        Raises IndexError if index is out of bounds.
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self._size:
            self.append(data)
            return
        prev = self._head
        for _ in range(index - 1):
            prev = prev.next  # type: ignore
        node = self._Node(data, prev.next)  # type: ignore
        prev.next = node  # type: ignore
        self._size += 1

    def pop(self, index: int = -1) -> Any:
        """
        Remove and return element at index (default: last). O(n).
        Raises IndexError if list is empty or index out of bounds.
        """
        if self._size == 0:
            raise IndexError("Pop from empty list")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            node = self._head
            assert node is not None
            self._head = node.next
            if self._size == 1:
                self._tail = None
            self._size -= 1
            return node.data
        prev = self._head
        for _ in range(index - 1):
            prev = prev.next  # type: ignore
        node = prev.next  # type: ignore
        prev.next = node.next  # type: ignore
        if node == self._tail:
            self._tail = prev
        self._size -= 1
        return node.data  # type: ignore

    def remove(self, value: Any) -> None:
        """
        Remove first occurrence of value. O(n).
        Raises ValueError if not found.
        """
        prev = None
        curr = self._head
        idx = 0
        while curr:
            if curr.data == value:
                if prev is None:
                    self._head = curr.next
                    if self._size == 1:
                        self._tail = None
                else:
                    prev.next = curr.next
                    if curr == self._tail:
                        self._tail = prev
                self._size -= 1
                return
            prev = curr
            curr = curr.next
            idx += 1
        raise ValueError(f"{value} not found in list")

    def get(self, index: int) -> Any:
        """
        Get value at index. O(n).
        Raises IndexError if out of bounds.
        """
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        node = self._head
        for _ in range(index):
            node = node.next  # type: ignore
        return node.data  # type: ignore

    def find(self, value: Any) -> int:
        """
        Return index of first occurrence of value, or -1 if not found. O(n).
        """
        curr = self._head
        idx = 0
        while curr:
            if curr.data == value:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def clear(self) -> None:
        """
        Remove all elements. O(1).
        """
        self._head = None
        self._tail = None
        self._size = 0

    def copy(self) -> 'SinglyLinkedList':
        """
        Return a shallow copy of the list. O(n).
        """
        return SinglyLinkedList(self)

    def __copy__(self) -> 'SinglyLinkedList':
        """
        Support for copy.copy(). O(n).
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'SinglyLinkedList':
        """
        Support for copy.deepcopy(). O(n).
        """
        copied = SinglyLinkedList()
        node = self._head
        while node:
            copied.append(deepcopy(node.data, memo))
            node = node.next
        return copied

    def reverse(self) -> None:
        """
        Reverse the list in place. O(n).
        """
        prev = None
        curr = self._head
        self._tail = self._head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self._head = prev

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Append all elements from iterable. O(n).
        """
        for item in iterable:
            self.append(item)

    def to_list(self) -> list[Any]:
        """
        Convert to Python list. O(n).
        """
        result = []
        node = self._head
        while node:
            result.append(node.data)
            node = node.next
        return result

    @classmethod
    def from_iterable(cls, iterable: Iterable[Any]) -> 'SinglyLinkedList':
        """
        Create list from iterable. O(n).
        """
        return cls(iterable)

    def __len__(self) -> int:
        """
        Return number of elements. O(1).
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterator over elements (forward). O(n).
        """
        node = self._head
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        String representation. O(n).
        """
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, index: int) -> Any:
        """
        Indexing: list[index]. O(n).
        """
        return self.get(index)

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Assign value at index. O(n).
        Raises IndexError if out of bounds.
        """
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        node = self._head
        for _ in range(index):
            node = node.next  # type: ignore
        node.data = value  # type: ignore

    def __eq__(self, other: object) -> bool:
        """
        Compare lists element-wise. O(n).
        """
        if not isinstance(other, SinglyLinkedList):
            return False
        if self._size != other._size:
            return False
        a = self._head
        b = other._head
        while a and b:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return True

    def contains(self, value: Any) -> bool:
        """
        Return True if value exists. O(n).
        """
        return self.find(value) != -1

    def count(self, value: Any) -> int:
        """
        Count occurrences of value. O(n).
        """
        cnt = 0
        node = self._head
        while node:
            if node.data == value:
                cnt += 1
            node = node.next
        return cnt

    def is_empty(self) -> bool:
        """
        Return True if list is empty. O(1).
        """
        return self._size == 0