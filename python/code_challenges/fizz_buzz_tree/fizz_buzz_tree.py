from code_challenges.stacks_and_queues.stacks_and_queues import Queue as Q

class Node:
  """Node class for K_ary_tree, (can be used for BinaryTree as well)
  """
  def __init__(self, value:int, first_child=None, next_sibling=None):
    """Node Instance for K_ary_Tree.

    Args:
        value (int, required): [expects only integers]. Defaults to None.
        first_child (Node, optional): [must be passed a Node]. Defaults to None
        next_sibling (Node, optional): [must be passed a Node]. Defaults to None
    """
    self.value = value
    self.first_child = first_child
    self.next_sibling = next_sibling

  def __str__(self):
    return f'Instance of Node value: {self.value} first_child: {self.first_child} next_sibling: {self.next_sibling}'
  
  def __repr__(self):
    return f'Instance of Node value: {self.value} first_child value: {self.first_child.value} next_sibling value: {self.next_sibling.value}'


class K_aryTree:
  """Allows creation of trees, whose nodes may have any number of children. 
  """

  def __init__(self):
    """Creates the Root node of the K_aryTree Tree. Defaults to None (empty)
    """
    self.root = None

  def __str_(self):
    return f'Instance of K_aryTree root: {self.root}'

  def __repr__(self):
    return f'Instance of K_aryTree root value: {self.root.value}'


  def breadth(self):
    by_layer = list()
    line_up = Q()
    line_up.enqueue(self.root)

    while line_up.is_empty() == False:
      curr = line_up.dequeue()
      if curr.first_child:
        line_up.enqueue(curr.first_child) 
      if curr.next_sibling:  
        line_up.enqueue(curr.next_sibling)  
      by_layer.append(curr.value)

    return by_layer


def fizz_buzz_tree(tree_star):
  line_up = Q()
  line_up.enqueue(tree_star.root)

  def _check_buzz(val):
    if val % 15:
      return 'FizzBuzz'
    if val % 3:
      return 'Fizz'
    if val % 5:
      return 'Buzz'
    else:
      return str(val)

# ok comment ramble, concept. I'm Queing nodes from base list. 
# if each node already knows is first child and next sibling than the only
# thing that needs to change is value assigned to it. 
# if the last thing I do in this traversal is reassign its value through the _check_buzz method. then append the entirety of the node to a List. 
# finally assign the first element of the list to the root of the new tree and viola ??? may be destructive. get it working then fix destruction. 
  ducky = []
  count = 0
  while line_up.is_empty() == False:
    curr = line_up.dequeue()
    temp_node = Node(_check_buzz(curr.value))
    ducky.append(temp_node)
    if curr.first_child:
      line_up.enqueue(curr.first_child)
      ducky[0].first_child = 
    if curr.next_sibling:
      line_up.enqueue(curr.next_sibling)

    count += 1
  fizzy_tree = K_aryTree()

   
    
      