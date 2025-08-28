from typing import Any, Optional, Iterator, Iterable
from copy import deepcopy

class DoublyLinkedList:
    """
    DoublyLinkedList implements a classic doubly linked list with a full Pythonic API.
    - Supports O(1) append, prepend, pop operations; O(n) insert, remove, find, and index-based access.
    - Iterator protocol (__iter__, __reversed__), rich comparison (__eq__), and list-like methods.
    - Data type: Any.
    """

    class _Node:
        __slots__ = ('data', 'prev', 'next')

        def __init__(self, data: Any, prev: Optional['DoublyLinkedList._Node'] = None, next: Optional['DoublyLinkedList._Node'] = None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize an empty list or fill from iterable.
        """
        self._head: Optional[DoublyLinkedList._Node] = None
        self._tail: Optional[DoublyLinkedList._Node] = None
        self._size: int = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, data: Any) -> None:
        """
        Add data to the end of the list. O(1).
        """
        node = self._Node(data)
        if not self._tail:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """
        Add data to the beginning of the list. O(1).
        """
        node = self._Node(data)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def insert(self, index: int, data: Any) -> None:
        """
        Insert data at given index. O(n).
        Raises IndexError if index is out of bounds.
        """
        if index < 0:
            index += self._size
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self._size:
            self.append(data)
            return
        curr = self._head
        for _ in range(index):
            curr = curr.next  # type: ignore
        node = self._Node(data, prev=curr.prev, next=curr)
        if curr.prev:
            curr.prev.next = node
        curr.prev = node
        if index == 0:
            self._head = node
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
            if self._head:
                self._head.prev = None
            if self._size == 1:
                self._tail = None
            self._size -= 1
            return node.data
        if index == self._size - 1:
            node = self._tail
            assert node is not None
            self._tail = node.prev
            if self._tail:
                self._tail.next = None
            if self._size == 1:
                self._head = None
            self._size -= 1
            return node.data
        curr = self._head
        for _ in range(index):
            curr = curr.next  # type: ignore
        assert curr is not None
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        self._size -= 1
        return curr.data

    def remove(self, value: Any) -> None:
        """
        Remove first occurrence of value. O(n).
        Raises ValueError if not found.
        """
        curr = self._head
        while curr:
            if curr.data == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self._head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self._tail = curr.prev
                self._size -= 1
                return
            curr = curr.next
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
        curr = self._head
        for _ in range(index):
            curr = curr.next  # type: ignore
        return curr.data  # type: ignore

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

    def copy(self) -> 'DoublyLinkedList':
        """
        Return a shallow copy of the list. O(n).
        """
        return DoublyLinkedList(self)

    def __copy__(self) -> 'DoublyLinkedList':
        """
        Support for copy.copy(). O(n).
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'DoublyLinkedList':
        """
        Support for copy.deepcopy(). O(n).
        """
        copied = DoublyLinkedList()
        curr = self._head
        while curr:
            copied.append(deepcopy(curr.data, memo))
            curr = curr.next
        return copied

    def reverse(self) -> None:
        """
        Reverse the list in place. O(n).
        """
        curr = self._head
        self._tail = self._head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            curr.prev = nxt
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
        curr = self._head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    @classmethod
    def from_iterable(cls, iterable: Iterable[Any]) -> 'DoublyLinkedList':
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
        curr = self._head
        while curr:
            yield curr.data
            curr = curr.next

    def __reversed__(self) -> Iterator[Any]:
        """
        Iterator over elements (backward). O(n).
        """
        curr = self._tail
        while curr:
            yield curr.data
            curr = curr.prev

    def __str__(self) -> str:
        """
        String representation. O(n).
        """
        return f"DoublyLinkedList([{', '.join(repr(x) for x in self)}])"

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
        curr = self._head
        for _ in range(index):
            curr = curr.next  # type: ignore
        curr.data = value  # type: ignore

    def __eq__(self, other: object) -> bool:
        """
        Compare lists element-wise. O(n).
        """
        if not isinstance(other, DoublyLinkedList):
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
        curr = self._head
        while curr:
            if curr.data == value:
                cnt += 1
            curr = curr.next
        return cnt

    def is_empty(self) -> bool:
        """
        Return True if list is empty. O(1).
        """
        return self._size == 0