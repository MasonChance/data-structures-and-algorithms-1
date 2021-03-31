import pytest
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import K_aryTree, fizz_buzz_tree, Node

def test_k_ary_tree_Node():
  actual = Node(3).__str__()
  expected = 'Instance of Node value: 3 first_child: None next_sibling: None'
  assert actual == expected

def test_k_ary_tree_init():
  actual = K_aryTree().root
  expected = None
  assert actual == expected

def test_k_ary_tree_root_assign():
  carey = K_aryTree()
  jim = Node(3)
  carey.root = jim
  actual = carey.root.value
  expected = 3
  assert actual == expected

def test_k_ary_tree_breadth_traverse(make_like_a_tree):
  actual = make_like_a_tree.breadth()
  expected = [3, 7, 10, 15, 13, 19]
  assert actual == expected 

def test_fizz_buzz_tree_six_nodes(make_like_a_tree):
  actual = fizz_buzz_tree(make_like_a_tree).breadth()
  expected = ['Fizz', '7', 'Buzz', 'FizzBuzz', '13', '19']
  assert actual == expected




# =========== Fixtures ==============
@pytest.fixture
def make_like_a_tree():
  carey = K_aryTree()
  jim = Node(3)
  bruce = Node(7)
  almighty = Node(10)
  morgan = Node(13)
  freeman = Node(15)
  jim.first_child = bruce
  jim.next_sibling = almighty
  bruce.first_child = freeman
  freeman.next_sibling = morgan
  morgan.next_sibling = Node(19)
  carey.root = jim
  return carey



