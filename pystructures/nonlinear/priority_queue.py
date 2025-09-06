from typing import Any, Optional, Iterable, Iterator, Callable, TypeVar, Type
from copy import deepcopy
from .heap import MaxHeap, MinHeap

T = TypeVar("T", bound="PriorityQueue")

class PriorityQueue:
    """
    PriorityQueue: classic stable priority queue built atop MinHeap/MaxHeap.
    - Stores (priority, value) pairs internally as (priority, insertion_index, value) for FIFO stability.
    - Custom key function supported for extracting priority from value.
    - O(log n) push/pop, O(1) peek, bulk and utility methods, rich comparison, copy/deepcopy, from_iterable.
    - Accepts any mutually comparable priority type; value can be any Python object.
    """

    def __init__(
        self,
        iterable: Optional[Iterable[Any]] = None,
        ascending: bool = True,
        key: Optional[Callable[[Any], Any]] = None
    ) -> None:
        """
        Initialize an empty priority queue or fill from iterable.
        :param iterable: Iterable of values or (priority, value) pairs.
        :param ascending: If True, lowest priority dequeued first (MinHeap); else highest (MaxHeap).
        :param key: Optional function to extract priority from value (if not given as pair).
        """
        self._heap = MinHeap() if ascending else MaxHeap()
        self._key = key
        self._counter = 0
        if iterable is not None:
            self.extend(iterable)

    def push(self, value: Any, priority: Optional[Any] = None) -> None:
        """
        Add an element with given priority (or compute via key).
        O(log n)
        :param value: Value to enqueue.
        :param priority: Priority for value. If None, uses key(value).
        :raises ValueError: If priority not given and no key set.
        """
        if priority is None:
            if self._key is None:
                raise ValueError("Either 'priority' or 'key' must be provided")
            priority = self._key(value)
        item = (priority, self._counter, value)
        self._heap.push(item)
        self._counter += 1

    def pop(self) -> Any:
        """
        Remove and return value with highest/lowest priority (depending on ascending).
        O(log n)
        :raises IndexError: If queue is empty.
        """
        _, _, value = self._heap.pop()
        return value

    def popitem(self) -> tuple[Any, Any]:
        """
        Remove and return (priority, value) pair.
        O(log n)
        :raises IndexError: If queue is empty.
        """
        priority, _, value = self._heap.pop()
        return (priority, value)

    def peek(self) -> Any:
        """
        Return value with highest/lowest priority without removing.
        O(1)
        :raises IndexError: If queue is empty.
        """
        _, _, value = self._heap.peek()
        return value

    def peekitem(self) -> tuple[Any, Any]:
        """
        Return (priority, value) pair without removing.
        O(1)
        :raises IndexError: If queue is empty.
        """
        priority, _, value = self._heap.peek()
        return (priority, value)

    def clear(self) -> None:
        """
        Remove all elements from the queue. O(1)
        """
        self._heap.clear()
        self._counter = 0

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Add all elements from iterable.
        Each element can be a value or (priority, value) pair.
        O(k log n)
        """
        for item in iterable:
            if (
                isinstance(item, tuple)
                and len(item) == 2
                and not isinstance(item[0], (str, bytes))
            ):
                priority, value = item
                self.push(value, priority)
            else:
                self.push(item)

    def to_list(self) -> list[Any]:
        """
        Return list of values in queue (internal heap order).
        O(n)
        """
        return [tup[2] for tup in self._heap.to_list()]

    def to_pair_list(self) -> list[tuple[Any, Any]]:
        """
        Return [(priority, value), ...] in internal heap order.
        O(n)
        """
        return [(tup[0], tup[2]) for tup in self._heap.to_list()]

    def copy(self: T) -> T:
        """
        Return a shallow copy of the priority queue. O(n)
        """
        copied = type(self)(
            ascending=isinstance(self._heap, MinHeap),
            key=self._key
        )
        copied._heap = self._heap.copy()
        copied._counter = self._counter
        return copied

    def __copy__(self: T) -> T:
        return self.copy()

    def __deepcopy__(self: T, memo) -> T:
        copied = type(self)(
            ascending=isinstance(self._heap, MinHeap),
            key=self._key
        )
        copied._heap = deepcopy(self._heap, memo)
        copied._counter = self._counter
        return copied

    @classmethod
    def from_iterable(
        cls: Type[T],
        iterable: Iterable[Any],
        ascending: bool = True,
        key: Optional[Callable[[Any], Any]] = None
    ) -> T:
        """
        Create a priority queue from iterable.
        Supports bulk insert of values or (priority, value) pairs.
        O(n)
        """
        pq = cls(ascending=ascending, key=key)
        pq.extend(iterable)
        return pq

    def count(self, value: Any) -> int:
        """
        Count occurrences of a value in the queue. O(n)
        """
        return sum(1 for tup in self._heap if tup[2] == value)

    def __contains__(self, value: Any) -> bool:
        """
        Return True if value exists in the queue. O(n)
        """
        return any(tup[2] == value for tup in self._heap)

    def __len__(self) -> int:
        """
        Return number of elements in the queue. O(1)
        """
        return len(self._heap)

    def is_empty(self) -> bool:
        """
        Return True if queue is empty. O(1)
        """
        return len(self._heap) == 0

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over values in internal heap order. O(n)
        """
        for tup in self._heap:
            yield tup[2]

    def __eq__(self, other: object) -> bool:
        """
        Compare queues element-wise. O(n)
        """
        if not isinstance(other, PriorityQueue):
            return False
        return self.to_pair_list() == other.to_pair_list()

    def __str__(self) -> str:
        """
        String representation. O(n)
        """
        return f"PriorityQueue([{', '.join(repr(x) for x in self)}])"

    def __repr__(self) -> str:
        return str(self)