import pytest
from pystructures.nonlinear import BinaryTree

def test_empty_tree():
    tree = BinaryTree()
    assert tree.is_empty()
    assert len(tree) == 0
    assert tree.root() is None
    assert list(tree) == []
    assert tree.to_list() == []
    tree.clear()
    assert tree.is_empty()

def test_init_from_iterable():
    tree = BinaryTree([1, 2, 3, 4])
    assert len(tree) == 4
    assert tree.root() is not None
    assert tree.to_list("levelorder") == [1, 2, 3, 4]
    assert tree.to_list("inorder") == [4, 2, 1, 3]

def test_from_level_order():
    tree = BinaryTree.from_level_order([10, 20, 30])
    assert isinstance(tree, BinaryTree)
    assert tree.to_list("levelorder") == [10, 20, 30]
    assert len(tree) == 3

def test_insert_left_right():
    tree = BinaryTree([1])
    root = tree.root()
    left = tree.insert_left(root, 2)
    right = tree.insert_right(root, 3)
    assert root.left is left and root.right is right
    assert tree.to_list("levelorder") == [1, 2, 3]
    assert len(tree) == 3

def test_extend_and_bulk_add():
    tree = BinaryTree([1])
    tree.extend([2, 3])
    assert tree.to_list("levelorder") == [1, 2, 3]
    tree.extend([])
    assert tree.to_list("levelorder") == [1, 2, 3]

def test_add_to_empty():
    tree = BinaryTree()
    tree.extend([7, 8])
    assert tree.to_list("levelorder") == [7, 8]
    assert len(tree) == 2

def test_contains_and_find():
    tree = BinaryTree([1, 2, 3])
    assert tree.contains(2)
    node_2 = tree.find(2)
    assert node_2 is not None
    assert node_2.data == 2
    assert not tree.contains(99)
    assert tree.find(99) is None
    assert tree.find_index(2) == 1
    assert tree.find_index(99) == -1
    assert 3 in tree
    assert 99 not in tree

def test_count():
    tree = BinaryTree([1, 2, 2, 3])
    assert tree.count(2) == 2
    assert tree.count(99) == 0

def test_remove_root_and_leaf():
    tree = BinaryTree([1, 2, 3, 4, 5])
    tree.remove(1)  # Remove root
    assert tree.to_list("levelorder").count(1) == 0
    tree.remove(4)  # Remove leaf
    assert tree.to_list("levelorder").count(4) == 0
    with pytest.raises(ValueError):
        tree.remove(99)

def test_remove_last_node():
    tree = BinaryTree([1])
    tree.remove(1)
    assert tree.is_empty()
    with pytest.raises(ValueError):
        tree.remove(1)

def test_traverse_orders():
    tree = BinaryTree([1, 2, 3, 4])
    assert list(tree.traverse("levelorder")) == [1, 2, 3, 4]
    assert list(tree.traverse("inorder")) == [4, 2, 1, 3]
    assert list(tree.traverse("preorder")) == [1, 2, 4, 3]
    assert list(tree.traverse("postorder")) == [4, 2, 3, 1]
    from collections.abc import Iterator
    assert isinstance(tree.traverse("reverselevelorder"), Iterator)
    with pytest.raises(ValueError):
        list(tree.traverse("unknown"))

def test_to_list_order():
    tree = BinaryTree([1, 2, 3])
    assert tree.to_list("levelorder") == [1, 2, 3]
    assert tree.to_list("inorder") == [2, 1, 3]

def test_equality_and_copying():
    tree1 = BinaryTree([1, 2, 3])
    tree2 = BinaryTree([1, 2, 3])
    assert tree1 == tree2
    tree3 = tree1.copy()
    assert tree1 == tree3
    tree3.remove(2)
    assert tree1 != tree3
    tree4 = tree1.__deepcopy__({})
    assert tree1 == tree4

def test_str_and_repr():
    tree = BinaryTree([1, "abc"])
    s = str(tree)
    r = repr(tree)
    assert s.startswith("BinaryTree")
    assert r.startswith("BinaryTree")
    assert "abc" in s

def test_iter_protocol():
    tree = BinaryTree([1, 2, 3])
    items = [x for x in tree]
    assert items == tree.to_list("inorder")

def test_clear_and_len():
    tree = BinaryTree([1, 2])
    tree.clear()
    assert tree.is_empty()
    assert len(tree) == 0
    tree.extend([5])
    assert len(tree) == 1

def test_height_and_properties():
    tree = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    assert tree.height() == 2
    assert tree.is_full()
    assert tree.is_perfect()
    tree.extend([8])
    assert not tree.is_perfect()
    assert tree.is_complete()
    assert tree.is_balanced()
    tree2 = BinaryTree([1,2,3,4,5,6,7,8,9,10])
    assert tree2.is_complete()
    assert not tree2.is_perfect()
    assert tree2.is_balanced()
    tree3 = BinaryTree([1,2,None,3])
    assert not tree3.is_full()
    assert not tree3.is_degenerate()

def test_degenerate_tree():
    tree = BinaryTree([1])
    node = tree.root()
    for i in range(2, 6):
        node = tree.insert_left(node, i)
    assert tree.is_degenerate()

def test_balance():
    tree = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    tree.extend([8,9,10,11,12,13,14])
    tree.balance()
    assert tree.is_balanced()

def test_boundary_and_diagonal():
    tree = BinaryTree([1, 2, 3, 4, 5])
    boundary = list(tree.traverse("boundary"))
    diagonal = list(tree.traverse("diagonal"))
    assert isinstance(boundary, list)
    assert isinstance(diagonal, list)
    assert len(boundary) > 0
    assert len(diagonal) > 0

def test_non_numeric_types():
    class Dummy: pass
    obj = Dummy()
    tree = BinaryTree(["a", obj, 3.14])
    assert "a" in tree
    assert obj in tree
    assert 3.14 in tree

def test_extend_empty_iterable():
    tree = BinaryTree([1])
    tree.extend([])
    assert tree.to_list("levelorder") == [1]

def test_remove_edge_cases():
    tree = BinaryTree([1, 2, 2, 3])
    tree.remove(2)
    assert tree.count(2) == 1
    tree.remove(2)
    assert tree.count(2) == 0
    # Removing from empty tree
    tree.clear()
    with pytest.raises(ValueError):
        tree.remove(2)