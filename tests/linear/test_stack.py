import pytest
from pystructures.linear import Stack

def test_push_and_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()

def test_peek():
    stack = Stack([1, 2])
    assert stack.peek() == 2
    stack.push(3)
    assert stack.peek() == 3
    stack.pop()
    assert stack.peek() == 2

def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()

def test_len_and_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    assert len(stack) == 1
    stack.pop()
    assert stack.is_empty()

def test_clear():
    stack = Stack([1, 2, 3])
    stack.clear()
    assert stack.is_empty()
    stack.push(4)
    assert stack.peek() == 4

def test_copy_and_equality():
    stack1 = Stack([1, 2, 3])
    stack2 = stack1.copy()
    assert stack1.to_list() == [3, 2, 1]
    assert stack2.to_list() == [3, 2, 1]
    assert stack1 == stack2
    stack2.push(4)
    assert stack1 != stack2

def test_deepcopy():
    import copy
    stack = Stack([[1], [2]])
    stack2 = copy.deepcopy(stack)
    assert stack.to_list() == [[2], [1]]
    assert stack2.to_list() == [[2], [1]]
    assert stack == stack2
    stack2.peek().append(99)
    assert stack != stack2

def test_iterator():
    stack = Stack([1, 2, 3])
    items = [x for x in stack]
    assert items == [3, 2, 1]

def test_extend_and_from_iterable():
    stack = Stack()
    stack.extend([1, 2, 3])
    assert list(stack) == [3, 2, 1]
    s2 = Stack.from_iterable([4, 5])
    assert list(s2) == [5, 4]
    stack.extend([])
    assert list(stack) == [3, 2, 1]

def test_to_list():
    stack = Stack([1, 2, 3])
    assert stack.to_list() == [3, 2, 1]

def test_contains_and_count():
    stack = Stack([1, "abc", None, "abc"])
    assert 1 in stack
    assert "abc" in stack
    assert stack.count("abc") == 2
    assert None in stack
    assert 42 not in stack

def test_find():
    stack = Stack([1, 2, 3, 2])
    assert stack.find(2) == 0
    assert stack.find(99) == -1

def test_get_and_indexing():
    stack = Stack([1, 2, 3])
    assert stack.get(0) == 3
    assert stack.get(1) == 2
    assert stack[2] == 1
    assert stack.get(-1) == 1
    assert stack.get(-2) == 2

def test_get_out_of_range():
    stack = Stack([1])
    with pytest.raises(IndexError):
        stack.get(5)
    with pytest.raises(IndexError):
        stack.get(-2)
    with pytest.raises(IndexError):
        _ = stack[2]
    with pytest.raises(IndexError):
        _ = stack[-2]

def test_str_and_repr():
    stack = Stack([1, 2])
    s = str(stack)
    r = repr(stack)
    assert s.startswith("Stack")
    assert r.startswith("Stack")

def test_bulk_operations_on_empty():
    stack = Stack()
    stack.extend([1, 2])
    assert list(stack) == [2, 1]
    stack.clear()
    stack.extend([])
    assert list(stack) == []
    stack2 = Stack.from_iterable([])
    assert list(stack2) == []

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    stack = Stack(["a", obj, 3.14])
    assert stack.find(obj) == 1
    assert stack.count("a") == 1
    assert "a" in stack
    assert 3.14 in stack
    assert obj in stack