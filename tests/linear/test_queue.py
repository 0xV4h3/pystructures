import pytest
from pystructures.linear import Queue

def test_enqueue_and_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert len(queue) == 3
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()

def test_front_and_rear():
    queue = Queue([1, 2])
    assert queue.front() == 1
    assert queue.rear() == 2
    queue.enqueue(3)
    assert queue.rear() == 3
    queue.dequeue()
    assert queue.front() == 2

def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_front_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.front()

def test_rear_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.rear()

def test_len_and_is_empty():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(1)
    assert not queue.is_empty()
    assert len(queue) == 1
    queue.dequeue()
    assert queue.is_empty()

def test_clear():
    queue = Queue([1, 2, 3])
    queue.clear()
    assert queue.is_empty()
    queue.enqueue(4)
    assert queue.front() == 4

def test_copy_and_equality():
    q1 = Queue([1, 2, 3])
    q2 = q1.copy()
    assert q1.to_list() == [1, 2, 3]
    assert q2.to_list() == [1, 2, 3]
    assert q1 == q2
    q2.enqueue(4)
    assert q1 != q2

def test_deepcopy():
    import copy
    queue = Queue([[1], [2]])
    queue2 = copy.deepcopy(queue)
    assert queue.to_list() == [[1], [2]]
    assert queue2.to_list() == [[1], [2]]
    assert queue == queue2
    queue2.front().append(99)
    assert queue != queue2

def test_extend_and_from_iterable():
    queue = Queue()
    queue.extend([1, 2, 3])
    assert queue.to_list() == [1, 2, 3]
    q2 = Queue.from_iterable([4, 5])
    assert q2.to_list() == [4, 5]
    queue.extend([])
    assert queue.to_list() == [1, 2, 3]

def test_to_list():
    queue = Queue([1, 2, 3])
    assert queue.to_list() == [1, 2, 3]

def test_contains_and_count():
    queue = Queue([1, "abc", None, "abc"])
    assert queue.contains(1)
    assert queue.contains("abc")
    assert queue.count("abc") == 2
    assert queue.contains(None)
    assert not queue.contains(42)
    assert 1 in queue
    assert "abc" in queue
    assert None in queue
    assert 42 not in queue

def test_str_and_repr():
    queue = Queue([1, 2])
    s = str(queue)
    r = repr(queue)
    assert s.startswith("Queue")
    assert r.startswith("Queue")

def test_bulk_operations_on_empty():
    queue = Queue()
    queue.extend([1, 2])
    assert queue.to_list() == [1, 2]
    queue.clear()
    queue.extend([])
    assert queue.to_list() == []
    queue2 = Queue.from_iterable([])
    assert queue2.to_list() == []

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    queue = Queue(["a", obj, 3.14])
    assert queue.count("a") == 1
    assert queue.contains("a")
    assert queue.contains(3.14)
    assert queue.contains(obj)

def test_eq_and_len():
    q1 = Queue([1, 2])
    q2 = Queue([1, 2])
    assert q1 == q2
    q2.dequeue()
    assert q1 != q2
    assert len(q2) == 1

def test_clear_and_is_empty():
    q = Queue([1, 2])
    q.clear()
    assert q.is_empty()
    assert len(q) == 0

def test_copy_independence():
    q1 = Queue([1, [2]])
    q2 = q1.copy()
    assert q1 == q2
    q2.dequeue()
    assert q1 != q2

def test_deepcopy_independence():
    import copy
    q1 = Queue([[1]])
    q2 = copy.deepcopy(q1)
    assert q1 == q2
    q2.front().append(2)
    assert q1 != q2