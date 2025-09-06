from typing import Any, Optional, Iterable, TypeVar, Type
from copy import deepcopy

T = TypeVar("T", bound="Queue")

class Queue:
    """
    Queue: classic FIFO container with a clean, minimal, and idiomatic API.
    - O(1) enqueue, dequeue, front, rear operations.
    - No iterator or index-based access.
    - Comparison, copy, bulk operations, and utility methods.
    - Stores any Python object.
    """

    class _Node:
        __slots__ = ('data', 'next')
        def __init__(self, data: Any, next: Optional['Queue._Node'] = None):
            self.data = data
            self.next = next

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize an empty queue or fill from iterable (left to right).
        The first element of iterable becomes the front of the queue.
        """
        self._front: Optional[Queue._Node] = None
        self._rear: Optional[Queue._Node] = None
        self._size: int = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def enqueue(self, data: Any) -> None:
        """
        Add data to the rear of the queue. O(1).
        """
        node = self._Node(data)
        if not self._front:
            self._front = self._rear = node
        else:
            assert self._rear is not None
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self) -> Any:
        """
        Remove and return the front element. Raises IndexError if empty. O(1).
        """
        if self._front is None:
            raise IndexError("Dequeue from empty queue")
        node = self._front
        self._front = node.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return node.data

    def front(self) -> Any:
        """
        Return the front element without removing. Raises IndexError if empty. O(1).
        """
        if self._front is None:
            raise IndexError("Front from empty queue")
        return self._front.data

    def rear(self) -> Any:
        """
        Return the rear element without removing. Raises IndexError if empty. O(1).
        """
        if self._rear is None:
            raise IndexError("Rear from empty queue")
        return self._rear.data

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty. O(1).
        """
        return self._size == 0

    def clear(self) -> None:
        """
        Remove all elements from the queue. O(1).
        """
        self._front = None
        self._rear = None
        self._size = 0

    def copy(self) -> T:
        """
        Return a shallow copy of the queue. O(n).
        """
        return Queue(self.to_list())

    def __copy__(self) -> T:
        return self.copy()

    def __deepcopy__(self, memo) -> T:
        items = [deepcopy(x, memo) for x in self.to_list()]
        return Queue(items)

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Enqueue all elements from iterable (left to right). O(n).
        """
        for item in iterable:
            self.enqueue(item)

    @classmethod
    def from_iterable(cls: Type[T], iterable: Iterable[Any]) -> T:
        """
        Create a queue from iterable. O(n).
        """
        return cls(iterable)

    def to_list(self) -> list[Any]:
        """
        Convert queue to Python list (front to rear). O(n).
        """
        result = []
        node = self._front
        while node:
            result.append(node.data)
            node = node.next
        return result

    def contains(self, value: Any) -> bool:
        """
        Return True if value exists in queue. O(n).
        """
        node = self._front
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
        node = self._front
        while node:
            if node.data == value:
                cnt += 1
            node = node.next
        return cnt

    def __contains__(self, value: Any) -> bool:
        return self.contains(value)

    def __len__(self) -> int:
        """
        Return the number of elements in the queue. O(1).
        """
        return self._size

    def __str__(self) -> str:
        """
        String representation. O(n).
        """
        return f"Queue([{', '.join(repr(x) for x in self.to_list())}])"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        """
        Compare queues element-wise. O(n).
        """
        if not isinstance(other, Queue):
            return False
        return self.to_list() == other.to_list()