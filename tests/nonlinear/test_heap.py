import pytest
from copy import copy, deepcopy
from pystructures.nonlinear import MaxHeap, MinHeap

def test_empty_heap_properties():
    maxh = MaxHeap()
    minh = MinHeap()
    assert len(maxh) == 0
    assert maxh.is_empty()
    assert list(maxh) == []
    assert maxh.to_list() == []
    assert 42 not in maxh
    assert maxh.count(42) == 0

def test_push_peek_pop():
    h = MaxHeap()
    h.push(5)
    h.push(10)
    h.push(1)
    assert h.peek() == 10
    assert h.pop() == 10
    assert h.peek() == 5
    assert h.pop() == 5
    assert h.pop() == 1
    with pytest.raises(IndexError):
        h.pop()
    with pytest.raises(IndexError):
        h.peek()

def test_minheap_order():
    h = MinHeap()
    for x in [8, 2, 5, 3]:
        h.push(x)
    assert h.peek() == 2
    assert sorted(h.to_list()) == [2, 3, 5, 8]
    assert h.pop() == 2
    assert h.peek() == 3

def test_extend_and_heapify():
    data = [7, 4, 9, 1]
    h1 = MaxHeap()
    h1.extend(data)
    assert sorted(h1.to_list(), reverse=True) == [9, 7, 4, 1]
    h2 = MaxHeap()
    h2.heapify(data)
    assert sorted(h2.to_list(), reverse=True) == [9, 7, 4, 1]
    h3 = MinHeap()
    h3.extend(data)
    assert sorted(h3.to_list()) == [1, 4, 7, 9]
    h4 = MinHeap()
    h4.heapify(data)
    assert sorted(h4.to_list()) == [1, 4, 7, 9]

def test_from_iterable():
    data = [5, 3, 8, 1]
    maxh = MaxHeap.from_iterable(data)
    minh = MinHeap.from_iterable(data)
    assert isinstance(maxh, MaxHeap)
    assert isinstance(minh, MinHeap)
    assert maxh.peek() == max(data)
    assert minh.peek() == min(data)
    assert set(list(maxh)) == set(data)
    assert set(list(minh)) == set(data)

def test_clear_and_is_empty():
    h = MaxHeap([3, 2, 1])
    assert not h.is_empty()
    h.clear()
    assert h.is_empty()
    with pytest.raises(IndexError):
        h.pop()
    with pytest.raises(IndexError):
        h.peek()

def test_copy_and_equality():
    orig = MinHeap([3, 2, 1])
    cp = orig.copy()
    assert type(cp) is MinHeap
    assert cp == orig
    cp.push(0)
    assert cp != orig
    orig.push(-1)
    assert cp != orig

def test_shallow_copy_and_eq():
    h1 = MaxHeap([1, 2, 3])
    h2 = h1.copy()
    assert h1 == h2
    h2.push(4)
    assert h1 != h2
    m1 = MinHeap([3, 2, 1])
    m2 = copy(m1)
    assert m1 == m2
    m2.pop()
    assert m1 != m2

def test_deepcopy_independence_with_lists():
    h1 = MaxHeap([[1, 2], [3, 4]])
    h2 = deepcopy(h1)
    assert h1 == h2
    found = False
    for i, item in enumerate(h2._data):
        if item == [1, 2]:
            h2._data[i].append(99)
            found = True
            break
    assert found
    assert any(x == [1, 2, 99] for x in h2._data)
    assert not any(x == [1, 2, 99] for x in h1._data)
    assert sorted([sorted(x) for x in h1._data]) != sorted([sorted(x) for x in h2._data])

def test_deepcopy_type_and_content():
    h = MaxHeap([1, 2])
    d = deepcopy(h)
    assert isinstance(d, MaxHeap)
    assert set(d.to_list()) == set(h.to_list())
    m = MinHeap([3, 1])
    d2 = deepcopy(m)
    assert isinstance(d2, MinHeap)
    assert set(d2.to_list()) == set(m.to_list())

def test_copy_empty_heap():
    h = MaxHeap()
    m = MinHeap()
    assert h.copy().is_empty()
    assert deepcopy(m).is_empty()

def test_copy_and_deepcopy_not_linked_with_lists():
    h = MaxHeap([[1]])
    h_shallow = copy(h)
    h_deep = deepcopy(h)
    assert h == h_shallow == h_deep
    h._data[0].append(42)
    assert 42 in h._data[0]
    assert 42 in h_shallow._data[0]
    assert 42 not in h_deep._data[0]
    h._data.append([99])
    assert [99] in h._data
    assert [99] not in h_shallow._data
    assert [99] not in h_deep._data

def test_copy_and_deepcopy_with_mutable_items():
    h = MaxHeap([[1], [2]])
    h_d = deepcopy(h)
    h_c = copy(h)
    found_deep = False
    found_shallow = False
    for i, item in enumerate(h_d._data):
        if item == [1]:
            h_d._data[i].append(999)
            found_deep = True
            break
    assert found_deep
    assert any(x == [1, 999] for x in h_d._data)
    assert not any(x == [1, 999] for x in h._data)
    for i, item in enumerate(h_c._data):
        if item == [2]:
            h_c._data[i].append(888)
            found_shallow = True
            break
    assert found_shallow
    assert any(x == [2, 888] for x in h._data)

def test_copy_and_deepcopy_minheap_with_lists():
    m = MinHeap([[1], [2]])
    m_d = deepcopy(m)
    m_c = copy(m)
    m_d._data[0].append(777)
    assert 777 not in m._data[0]
    m_c._data[0].append(555)
    assert 555 in m._data[0]
    assert m_d._data[0] == [1, 777]

def test_typeerror_on_non_comparable_dict():
    with pytest.raises(TypeError):
        MinHeap([{"a": 1}, {"b": 2}])
    with pytest.raises(TypeError):
        MaxHeap([{"a": 1}, {"b": 2}])

def test_typeerror_on_non_comparable_dummy():
    class Dummy: pass
    obj1 = Dummy()
    obj2 = Dummy()
    with pytest.raises(TypeError):
        MaxHeap([obj1, obj2])
    with pytest.raises(TypeError):
        MinHeap([obj1, obj2])

def test_typeerror_on_module_objects():
    import sys
    with pytest.raises(TypeError):
        MaxHeap([sys, sys])
    with pytest.raises(TypeError):
        MinHeap([sys, sys])
    h = MaxHeap([1, 2])
    h._data.append(sys)
    with pytest.raises(TypeError):
        deepcopy(h)

def test_to_list_and_iteration():
    h = MaxHeap([1, 2, 3])
    items = list(h)
    pylist = h.to_list()
    assert set(items) == set([1, 2, 3])
    assert set(pylist) == set([1, 2, 3])

def test_contains_and_count():
    h = MinHeap([1, 2, 2, 3])
    assert 2 in h
    assert h.count(2) == 2
    assert 4 not in h
    assert h.count(4) == 0

def test_bulk_operations_on_empty():
    h = MaxHeap()
    h.extend([1, 2])
    assert set(h.to_list()) == {1, 2}
    h.clear()
    h.extend([])
    assert h.to_list() == []
    h2 = MaxHeap.from_iterable([])
    assert h2.to_list() == []

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    import pytest
    with pytest.raises(TypeError):
        MinHeap(["a", obj, 3.14])

def test_exceptions():
    h = MaxHeap()
    with pytest.raises(IndexError):
        h.pop()
    with pytest.raises(IndexError):
        h.peek()
    h.push(1)
    h.pop()
    with pytest.raises(IndexError):
        h.pop()

def test_bulk_heapify_performance_and_correctness():
    data = list(range(1000))
    h = MinHeap()
    h.heapify(data)
    assert h.peek() == 0
    assert set(h.to_list()) == set(data)
    sorted_out = [h.pop() for _ in range(len(data))]
    assert sorted_out == sorted(data)

def test_typevar_self_usage():
    maxh = MaxHeap([1, 2, 3])
    minh = MinHeap([3, 2, 1])
    maxh2 = maxh.copy()
    minh2 = minh.copy()
    assert isinstance(maxh2, MaxHeap)
    assert isinstance(minh2, MinHeap)
    maxh3 = MaxHeap.from_iterable([4, 5])
    minh3 = MinHeap.from_iterable([5, 4])
    assert isinstance(maxh3, MaxHeap)
    assert isinstance(minh3, MinHeap)
    assert maxh2.peek() == max([1, 2, 3])
    assert minh2.peek() == min([3, 2, 1])