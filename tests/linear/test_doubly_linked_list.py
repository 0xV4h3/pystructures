import pytest
from pystructures.linear import DoublyLinkedList

def test_append_and_to_list():
    lst = DoublyLinkedList()
    lst.append(1)
    lst.append(2)
    assert lst.to_list() == [1, 2]

def test_prepend():
    lst = DoublyLinkedList()
    lst.prepend(1)
    lst.prepend(2)
    assert lst.to_list() == [2, 1]

def test_insert():
    lst = DoublyLinkedList([1, 3])
    lst.insert(1, 2)
    assert lst.to_list() == [1, 2, 3]

def test_insert_out_of_range():
    lst = DoublyLinkedList([1, 2])
    with pytest.raises(IndexError):
        lst.insert(5, 99)
    with pytest.raises(IndexError):
        lst.insert(-4, 99)

def test_pop():
    lst = DoublyLinkedList([1, 2, 3])
    assert lst.pop() == 3
    assert lst.to_list() == [1, 2]
    assert lst.pop(0) == 1
    assert lst.to_list() == [2]

def test_pop_out_of_range():
    lst = DoublyLinkedList([1])
    with pytest.raises(IndexError):
        lst.pop(5)
    lst.clear()
    with pytest.raises(IndexError):
        lst.pop()

def test_remove():
    lst = DoublyLinkedList([1, 2, 3])
    lst.remove(2)
    assert lst.to_list() == [1, 3]
    with pytest.raises(ValueError):
        lst.remove(99)

def test_indexing():
    lst = DoublyLinkedList([1, 2, 3])
    assert lst[0] == 1
    lst[1] = 99
    assert lst[1] == 99

def test_indexing_out_of_range():
    lst = DoublyLinkedList([1])
    with pytest.raises(IndexError):
        _ = lst[2]
    with pytest.raises(IndexError):
        lst[2] = 5

def test_len_and_is_empty():
    lst = DoublyLinkedList()
    assert lst.is_empty()
    lst.append(1)
    assert len(lst) == 1
    assert not lst.is_empty()

def test_reverse():
    lst = DoublyLinkedList([1, 2, 3])
    lst.reverse()
    assert lst.to_list() == [3, 2, 1]

def test_copy_and_equality():
    lst1 = DoublyLinkedList([1, 2])
    lst2 = lst1.copy()
    assert lst1 == lst2
    lst2.append(3)
    assert lst1 != lst2

def test_find_and_count():
    lst = DoublyLinkedList([1, 2, 2, 3])
    assert lst.find(2) == 1
    assert lst.count(2) == 2
    assert lst.find(99) == -1

def test_clear():
    lst = DoublyLinkedList([1, 2, 3])
    lst.clear()
    assert lst.is_empty()
    lst.append(7)
    assert lst.to_list() == [7]

def test_get_negative_index():
    lst = DoublyLinkedList([1, 2, 3])
    assert lst.get(-1) == 3
    assert lst.get(-2) == 2

def test_get_out_of_range():
    lst = DoublyLinkedList([1])
    with pytest.raises(IndexError):
        lst.get(10)
    with pytest.raises(IndexError):
        lst.get(-2)

def test_negative_indexing():
    lst = DoublyLinkedList([1, 2, 3])
    assert lst[-1] == 3
    assert lst[-2] == 2
    lst[-3] = 99
    assert lst[0] == 99

def test_extend_and_from_iterable():
    lst = DoublyLinkedList([1])
    lst.extend([2, 3])
    assert lst.to_list() == [1, 2, 3]
    lst2 = DoublyLinkedList.from_iterable([4, 5])
    assert lst2.to_list() == [4, 5]
    lst3 = DoublyLinkedList()
    lst3.extend([])
    assert lst3.to_list() == []

def test_contains_operator():
    lst = DoublyLinkedList([1, "abc", None])
    assert 1 in lst
    assert "abc" in lst
    assert None in lst
    assert 42 not in lst

def test_str_and_repr():
    lst = DoublyLinkedList([1, 2])
    s = str(lst)
    r = repr(lst)
    assert s.startswith("DoublyLinkedList")
    assert r.startswith("DoublyLinkedList")

def test_iteration():
    lst = DoublyLinkedList([1, 2, 3])
    items = [x for x in lst]
    assert items == [1, 2, 3]

def test_reverse_iteration():
    lst = DoublyLinkedList([1, 2, 3])
    items = [x for x in reversed(lst)]
    assert items == [3, 2, 1]

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    lst = DoublyLinkedList(["a", obj, 3.14])
    assert lst[1] is obj
    assert "a" in lst
    assert 3.14 in lst

def test_bulk_operations_on_empty():
    lst = DoublyLinkedList()
    lst.extend([1, 2])
    assert lst.to_list() == [1, 2]
    lst.clear()
    lst.extend([])
    assert lst.to_list() == []
    lst2 = DoublyLinkedList.from_iterable([])
    assert lst2.to_list() == []