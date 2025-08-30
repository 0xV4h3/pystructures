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

def test_extend_and_from_iterable():
    stack = Stack()
    stack.extend([1, 2, 3])
    assert stack.to_list() == [3, 2, 1]
    s2 = Stack.from_iterable([4, 5])
    assert s2.to_list() == [5, 4]
    stack.extend([])
    assert stack.to_list() == [3, 2, 1]

def test_to_list():
    stack = Stack([1, 2, 3])
    assert stack.to_list() == [3, 2, 1]

def test_contains_and_count():
    stack = Stack([1, "abc", None, "abc"])
    assert stack.contains(1)
    assert stack.contains("abc")
    assert stack.count("abc") == 2
    assert stack.contains(None)
    assert not stack.contains(42)
    assert 1 in stack
    assert "abc" in stack
    assert None in stack
    assert 42 not in stack

def test_str_and_repr():
    stack = Stack([1, 2])
    s = str(stack)
    r = repr(stack)
    assert s.startswith("Stack")
    assert r.startswith("Stack")

def test_bulk_operations_on_empty():
    stack = Stack()
    stack.extend([1, 2])
    assert stack.to_list() == [2, 1]
    stack.clear()
    stack.extend([])
    assert stack.to_list() == []
    stack2 = Stack.from_iterable([])
    assert stack2.to_list() == []

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    stack = Stack(["a", obj, 3.14])
    assert stack.count("a") == 1
    assert stack.contains("a")
    assert stack.contains(3.14)
    assert stack.contains(obj)

def test_eq_and_len():
    s1 = Stack([1, 2])
    s2 = Stack([1, 2])
    assert s1 == s2
    s2.pop()
    assert s1 != s2
    assert len(s2) == 1

def test_clear_and_is_empty():
    s = Stack([1, 2])
    s.clear()
    assert s.is_empty()
    assert len(s) == 0

def test_copy_independence():
    s1 = Stack([1, [2]])
    s2 = s1.copy()
    assert s1 == s2
    s2.pop()
    assert s1 != s2

def test_deepcopy_independence():
    import copy
    s1 = Stack([[1]])
    s2 = copy.deepcopy(s1)
    assert s1 == s2
    s2.peek().append(2)
    assert s1 != s2