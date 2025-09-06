import pytest
from pystructures.nonlinear import PriorityQueue

def test_empty_queue():
    pq = PriorityQueue()
    assert pq.is_empty()
    assert len(pq) == 0
    with pytest.raises(IndexError):
        pq.pop()
    with pytest.raises(IndexError):
        pq.peek()
    with pytest.raises(IndexError):
        pq.popitem()
    with pytest.raises(IndexError):
        pq.peekitem()
    pq.clear()  # Should not error on empty

def test_push_and_peek_pop():
    pq = PriorityQueue()
    pq.push("a", priority=2)
    pq.push("b", priority=1)
    pq.push("c", priority=3)
    assert len(pq) == 3
    assert pq.peek() == "b"
    assert pq.peekitem() == (1, "b")
    assert pq.pop() == "b"
    assert pq.popitem() == (2, "a")
    assert pq.pop() == "c"
    assert pq.is_empty()

def test_fifo_stability():
    pq = PriorityQueue()
    pq.push("first", priority=5)
    pq.push("second", priority=5)
    pq.push("third", priority=5)
    assert pq.pop() == "first"
    assert pq.pop() == "second"
    assert pq.pop() == "third"

def test_extend_with_pairs_and_values():
    pq = PriorityQueue()
    pq.extend([(1, "a"), (3, "c"), (2, "b")])
    with pytest.raises(ValueError):
        pq.extend(["d"])  # Should raise ValueError if no key is set
    assert sorted(pq.to_list()) == ["a", "b", "c"]

def test_custom_key_function():
    pq = PriorityQueue(key=len)
    pq.push("aaa")
    pq.push("bb")
    pq.push("c")
    assert pq.peek() == "c"
    assert pq.pop() == "c"
    assert pq.pop() == "bb"
    assert pq.pop() == "aaa"
    assert pq.is_empty()

def test_count_and_contains():
    pq = PriorityQueue()
    pq.push("a", priority=1)
    pq.push("b", priority=2)
    pq.push("a", priority=3)
    assert pq.count("a") == 2
    assert "a" in pq
    assert "b" in pq
    assert "c" not in pq

def test_clear_and_len():
    pq = PriorityQueue()
    pq.push("a", priority=1)
    pq.push("b", priority=2)
    assert len(pq) == 2
    pq.clear()
    assert pq.is_empty()
    assert len(pq) == 0

def test_to_list_to_pair_list():
    pq = PriorityQueue()
    pq.push("x", priority=9)
    pq.push("y", priority=7)
    lst = pq.to_list()
    assert "x" in lst and "y" in lst
    pairs = pq.to_pair_list()
    assert (9, "x") in pairs and (7, "y") in pairs

def test_copy_and_deepcopy():
    import copy
    pq = PriorityQueue()
    pq.push([1, 2], priority=5)
    pq.push([3, 4], priority=1)
    pq2 = pq.copy()
    assert pq2 == pq
    pq2.pop()
    assert pq2 != pq
    pq3 = copy.deepcopy(pq)
    assert pq3 == pq
    pq3.pop()
    assert pq3 != pq

def test_from_iterable_and_bulk():
    data = [(2, "b"), (1, "a"), (3, "c")]
    pq = PriorityQueue.from_iterable(data)
    assert pq.pop() == "a"
    assert pq.pop() == "b"
    assert pq.pop() == "c"
    assert pq.is_empty()

def test_equality_and_str_repr():
    pq1 = PriorityQueue()
    pq2 = PriorityQueue()
    pq1.push("a", priority=1)
    pq2.push("a", priority=1)
    assert pq1 == pq2
    pq2.push("b", priority=2)
    assert pq1 != pq2
    s = str(pq1)
    r = repr(pq1)
    assert s.startswith("PriorityQueue")
    assert r.startswith("PriorityQueue")

def test_priority_types_comparable():
    pq = PriorityQueue()
    pq.push("a", priority=1)
    pq.push("b", priority=2)
    with pytest.raises(TypeError):
        pq.push("c", priority="high")  # int and str are not comparable

def test_ascending_and_descending():
    pq_min = PriorityQueue(ascending=True)
    pq_max = PriorityQueue(ascending=False)
    for prio, val in [(1, "a"), (3, "c"), (2, "b")]:
        pq_min.push(val, priority=prio)
        pq_max.push(val, priority=prio)
    assert pq_min.pop() == "a"  # min priority first
    assert pq_max.pop() == "c"  # max priority first

def test_bulk_extend_mixed_pairs_and_values():
    pq = PriorityQueue(key=lambda x: x[1])
    pq.extend([("v1", 1), ("v2", 2)])
    pq.push(("v0", 0))
    assert pq.pop()[0] == "v0"
    assert pq.pop()[0] == "v1"
    assert pq.pop()[0] == "v2"
    assert pq.is_empty()

def test_mutable_values():
    pq = PriorityQueue()
    d = {"x": 1}
    pq.push(d, priority=1)
    d["y"] = 2
    assert pq.peek() == d  # Should reflect mutation

def test_edge_priority_none_and_key_missing():
    pq = PriorityQueue()
    with pytest.raises(ValueError):
        pq.push("a")  # No priority, no key

def test_priorityqueue_repr_and_str_nonempty():
    pq = PriorityQueue()
    pq.push("a", priority=1)
    pq.push("b", priority=2)
    s = str(pq)
    r = repr(pq)
    assert "PriorityQueue" in s
    assert "PriorityQueue" in r

def test_iteration_protocol():
    pq = PriorityQueue()
    pq.push("a", priority=1)
    pq.push("b", priority=2)
    items = [x for x in pq]
    assert set(items) == {"a", "b"}