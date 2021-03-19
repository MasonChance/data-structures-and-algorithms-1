import pytest
from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.tree.tree import BinaryTree, Node

@pytest.fixture 
def b1nary():
    bin_tree = BinaryTree()
    bin_tree.root = Node(5)
    bin_tree.root.left = Node(3)
    bin_tree.root.right = Node(9)
    bin_tree.root.left.left = Node(1)
    bin_tree.root.right.left = Node(7)

    return bin_tree


@pytest.fixture 
def binary_t():
    bin_tree = BinaryTree()
    bin_tree.root = Node(4)
    bin_tree.root.left = Node(1)
    bin_tree.root.left.right = Node(2)
    bin_tree.root.right = Node(5)
    bin_tree.root.right.right = Node(7)

    return bin_tree


def test_tree_intersection_ouput_type(b1nary, binary_t):
    bt1 = b1nary
    bt2 = binary_t
    com_val = tree_intersection(bt1, bt2)
    actual = str(type(com_val))
    expected = "<class 'list'>"
    assert actual == expected


def test_tree_intersection_empty_input(b1nary):
    bt1 = b1nary
    bt2 = BinaryTree()
    with pytest.raises(ValueError) as excinfo:
        tree_intersection(bt1, bt2)
    
    actual = str(excinfo.value)
    expected = 'cannot operate on an empty tree'
    assert actual == expected


def test_tree_intersection(b1nary, binary_t):
    com_val_list = tree_intersection(b1nary, binary_t)
    actual = com_val_list
    expected = [1, 5, 7]
    assert actual == expected



    

    
