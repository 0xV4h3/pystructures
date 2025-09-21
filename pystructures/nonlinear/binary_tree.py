from typing import Any, Optional, Iterable, Iterator, TypeVar, Type, Tuple, Deque
from collections import deque
from copy import deepcopy

T = TypeVar("T", bound="BinaryTree")

class BinaryTree:
    """
    Classic binary tree with no ordering constraint.
    Supports arbitrary insertions, traversals, copying, comparison, bulk and utility operations.
    """

    class _Node:
        __slots__ = ("data", "left", "right")
        def __init__(self, data: Any, left: Optional["_Node"] = None, right: Optional["_Node"] = None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        """
        Initialize tree. If iterable is given, build tree via level-order.
        O(n)
        """
        self._root: Optional["_Node"] = None
        self._size: int = 0
        if iterable is not None:
            items = list(iterable)
            self._root = self._build_level_order(items)
            self._size = len(items)

    @classmethod
    def from_level_order(cls: Type[T], iterable: Iterable[Any]) -> T:
        """
        Build a complete binary tree from iterable (level order).
        O(n)
        """
        items = list(iterable)
        tree = cls()
        tree._root = tree._build_level_order(items)
        tree._size = len(items)
        return tree

    def _build_level_order(self, items: list[Any]) -> Optional["_Node"]:
        """
        Internal: Build tree from list of items (level-order).
        O(n)
        """
        if not items:
            return None
        nodes = [self._Node(v) for v in items]
        for i, node in enumerate(nodes):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
        return nodes[0]

    def insert_left(self, parent: "_Node", value: Any) -> "_Node":
        """
        Insert value as left child of parent.
        O(1)
        """
        node = self._Node(value)
        parent.left = node
        self._size += 1
        return node

    def insert_right(self, parent: "_Node", value: Any) -> "_Node":
        """
        Insert value as right child of parent.
        O(1)
        """
        node = self._Node(value)
        parent.right = node
        self._size += 1
        return node

    def root(self) -> Optional["_Node"]:
        """
        Return root node.
        O(1)
        """
        return self._root

    def is_empty(self) -> bool:
        """
        Return True if tree is empty.
        O(1)
        """
        return self._size == 0

    def clear(self) -> None:
        """
        Remove all nodes.
        O(1)
        """
        self._root = None
        self._size = 0

    def copy(self: T) -> T:
        """
        Return a shallow copy of the tree.
        O(n)
        """
        return type(self).from_level_order(self.to_list("levelorder"))

    def __copy__(self: T) -> T:
        """
        Support for copy.copy().
        O(n)
        """
        return self.copy()

    def __deepcopy__(self: T, memo) -> T:
        """
        Support for copy.deepcopy().
        O(n)
        """
        items = deepcopy(self.to_list("levelorder"), memo)
        return type(self).from_level_order(items)

    def __eq__(self, other: object) -> bool:
        """
        Compare trees element-wise and structure-wise.
        O(n)
        """
        if not isinstance(other, BinaryTree):
            return False
        return self.to_list("levelorder") == other.to_list("levelorder")

    def __len__(self) -> int:
        """
        Return number of elements. O(1)
        """
        return self._size

    def find(self, value: Any) -> Optional["_Node"]:
        """
        Return reference to the first node containing value in level-order traversal.
        Returns None if not found.
        O(n)
        """
        if not self._root:
            return None
        queue: Deque["_Node"] = deque([self._root])
        while queue:
            node = queue.popleft()
            if node.data == value:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    def find_index(self, value: Any) -> int:
        """
        Return index of first occurrence of value in level-order traversal, or -1 if not found.
        O(n)
        """
        if not self._root:
            return -1
        queue: Deque["_Node"] = deque([self._root])
        idx = 0
        while queue:
            node = queue.popleft()
            if node.data == value:
                return idx
            idx += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return -1

    def contains(self, value: Any) -> bool:
        """
        Return True if value exists in the tree. O(n)
        """
        return self.find(value) is not None

    def __contains__(self, value: Any) -> bool:
        """
        Operator support for `value in tree`. O(n)
        """
        return self.contains(value)

    def count(self, value: Any) -> int:
        """
        Count occurrences of value in the tree.
        O(n)
        """
        return sum(1 for x in self.traverse("levelorder") if x == value)

    def extend(self, iterable: Iterable[Any]) -> None:
        """
        Add all elements from iterable to the tree in level-order fashion.
        O(k * n), where k = number of new items, n = current size.
        """
        for value in iterable:
            self._add_level_order(value)
            self._size += 1

    def _add_level_order(self, value: Any) -> None:
        """
        Insert value at the first available position in level-order (BFS).
        """
        node = self._Node(value)
        if self._root is None:
            self._root = node
            return
        queue: Deque["_Node"] = deque([self._root])
        while queue:
            curr = queue.popleft()
            if curr.left is None:
                curr.left = node
                return
            else:
                queue.append(curr.left)
            if curr.right is None:
                curr.right = node
                return
            else:
                queue.append(curr.right)

    def remove(self, value: Any) -> None:
        """
        Remove first occurrence of value in level-order traversal.
        Replaces removed node with deepest node to preserve completeness.
        Raises ValueError if not found.
        O(n)
        """
        if not self._root:
            raise ValueError(f"{value} not found in tree")

        queue: Deque[Tuple["_Node", Optional["_Node"]]] = deque([(self._root, None)])
        target: Optional["_Node"] = None
        target_parent: Optional["_Node"] = None
        deepest: Optional["_Node"] = None
        deepest_parent: Optional["_Node"] = None

        while queue:
            node, parent = queue.popleft()
            if node.data == value and target is None:
                target = node
                target_parent = parent
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
            deepest = node
            deepest_parent = parent

        if not target:
            raise ValueError(f"{value} not found in tree")

        if deepest is target:
            if target_parent is None:
                self._root = None
            else:
                if target_parent.left is target:
                    target_parent.left = None
                else:
                    target_parent.right = None
            self._size -= 1
            return

        target.data = deepest.data
        if deepest_parent.left is deepest:
            deepest_parent.left = None
        else:
            deepest_parent.right = None
        self._size -= 1

    def to_list(self, order: str = "inorder") -> list[Any]:
        """
        Convert tree to list in given traversal order.
        O(n)
        """
        return list(self.traverse(order))

    def traverse(self, order: str = "inorder") -> Iterator[Any]:
        """
        Traverse tree in given order.
        Supported: inorder, preorder, postorder, levelorder, reverselevelorder, boundary, diagonal.
        O(n)
        """
        if not self._root:
            return iter([])
        if order == "inorder":
            return self._inorder(self._root)
        elif order == "preorder":
            return self._preorder(self._root)
        elif order == "postorder":
            return self._postorder(self._root)
        elif order == "levelorder":
            return self._levelorder(self._root)
        elif order == "reverselevelorder":
            return self._reverselevelorder(self._root)
        elif order == "boundary":
            return self._boundary(self._root)
        elif order == "diagonal":
            return self._diagonal(self._root)
        else:
            raise ValueError(f"Unknown traversal order: {order}")

    def _inorder(self, node: "_Node") -> Iterator[Any]:
        if node.left:
            yield from self._inorder(node.left)
        yield node.data
        if node.right:
            yield from self._inorder(node.right)

    def _preorder(self, node: "_Node") -> Iterator[Any]:
        yield node.data
        if node.left:
            yield from self._preorder(node.left)
        if node.right:
            yield from self._preorder(node.right)

    def _postorder(self, node: "_Node") -> Iterator[Any]:
        if node.left:
            yield from self._postorder(node.left)
        if node.right:
            yield from self._postorder(node.right)
        yield node.data

    def _levelorder(self, node: "_Node") -> Iterator[Any]:
        queue: Deque["_Node"] = deque([node])
        while queue:
            curr = queue.popleft()
            yield curr.data
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def _reverselevelorder(self, node: "_Node") -> Iterator[Any]:
        queue: Deque["_Node"] = deque([node])
        stack: list[Any] = []
        while queue:
            curr = queue.popleft()
            stack.append(curr.data)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        while stack:
            yield stack.pop()

    def _boundary(self, node: "_Node") -> Iterator[Any]:
        curr = node
        while curr:
            yield curr.data
            curr = curr.left
        def leaves(n: Optional["_Node"]):
            if n:
                if not n.left and not n.right:
                    yield n.data
                yield from leaves(n.left)
                yield from leaves(n.right)
        yield from leaves(node.left)
        yield from leaves(node.right)
        rights: list[Any] = []
        curr = node.right
        while curr:
            rights.append(curr.data)
            curr = curr.right
        for d in reversed(rights):
            yield d

    def _diagonal(self, node: "_Node") -> Iterator[Any]:
        def helper(queue: list["_Node"]):
            while queue:
                curr = queue.pop(0)
                while curr:
                    yield curr.data
                    if curr.left:
                        queue.append(curr.left)
                    curr = curr.right
        return helper([node])

    def __iter__(self) -> Iterator[Any]:
        """
        Default iterator (inorder).
        O(n)
        """
        return self.traverse("inorder")

    def __str__(self) -> str:
        """
        String representation. O(n)
        """
        return f"BinaryTree([{', '.join(repr(x) for x in self)}])"

    def __repr__(self) -> str:
        return str(self)

    def is_full(self) -> bool:
        """
        Return True if tree is full (every node has 0 or 2 children).
        O(n)
        """
        def _full(node: Optional["_Node"]) -> bool:
            if not node:
                return True
            if bool(node.left) != bool(node.right):
                return False
            return _full(node.left) and _full(node.right)
        return _full(self._root)

    def is_perfect(self) -> bool:
        """
        Return True if tree is perfect (all leaves at same depth, every node has 2 children).
        O(n)
        """
        def _depth(node: Optional["_Node"]) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d
        def _perfect(node: Optional["_Node"], depth: int, level: int=1) -> bool:
            if not node:
                return True
            if not node.left and not node.right:
                return depth == level
            if not node.left or not node.right:
                return False
            return _perfect(node.left, depth, level+1) and _perfect(node.right, depth, level+1)
        d = _depth(self._root)
        return _perfect(self._root, d)

    def is_complete(self) -> bool:
        """
        Return True if tree is complete (all levels except last are full, last level filled left to right).
        O(n)
        """
        if not self._root:
            return True
        queue: Deque["_Node"] = deque([self._root])
        end = False
        while queue:
            node = queue.popleft()
            if node.left:
                if end:
                    return False
                queue.append(node.left)
            else:
                end = True
            if node.right:
                if end:
                    return False
                queue.append(node.right)
            else:
                end = True
        return True

    def is_balanced(self) -> bool:
        """
        Return True if tree is height-balanced (difference <= 1 for any node).
        O(n)
        """
        def _balanced(node: Optional["_Node"]) -> Tuple[bool, int]:
            if not node:
                return True, -1
            left_bal, left_h = _balanced(node.left)
            right_bal, right_h = _balanced(node.right)
            balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
            return balanced, 1 + max(left_h, right_h)
        return _balanced(self._root)[0]

    def is_degenerate(self) -> bool:
        """
        Return True if tree is degenerate (each parent has only one child).
        O(n)
        """
        def _degenerate(node: Optional["_Node"]) -> bool:
            if not node:
                return True
            if node.left and node.right:
                return False
            return _degenerate(node.left) and _degenerate(node.right)
        return _degenerate(self._root)

    def height(self) -> int:
        """
        Return height of the tree.
        O(n)
        """
        def _height(node: Optional["_Node"]) -> int:
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self._root)

    def balance(self) -> None:
        """
        Balance tree by rebuilding as complete binary tree from inorder traversal.
        O(n)
        """
        items = self.to_list("inorder")
        def build(items: list[Any]) -> Optional["_Node"]:
            if not items:
                return None
            mid = len(items) // 2
            root = self._Node(items[mid])
            root.left = build(items[:mid])
            root.right = build(items[mid+1:])
            return root
        self._root = build(items)