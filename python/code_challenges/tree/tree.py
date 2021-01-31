class Node:
  """Creates an instance of Node for use in BinaryTree
  """
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return f'A binary Tree Node value of {self.value}'

  def __repr__(self):
    return f'A binary Tree Node value of {self.value}'

class BinaryTree:
  """Creates an empty BinaryTree instance, and holds methods for traversal as well as adding nodes to the Tree. for use with BinarySearchTree
  """
  def __init__(self):
    self.root=None
    

  def __str__(self):
    return f'An instance of a BinaryTree, root is {self.root}'

  def __repr__(self):
    return f'An instance of a BinaryTree, root is {self.root.value}'
  
  def pre_order(self):
    def traverse(root, result=[]):
      if not root:
        return  
      result.append(root.value)
      if root.left:
        traverse(root.left, result)
      if root.right:
        traverse(root.right, result)
      return result
    return traverse(self.root)

  def in_order(self):
    def traverse(root, result=[]):
      if not root:
        return
      if root.left:
        traverse(root.left, result)
      result.append(root.value)
      if root.right:
        traverse(root.right, result)
      return result
    return traverse(self.root)


  def post_order(self):
    def traverse(root, result=[]):
      if not root:
        return
      if root.left:
        traverse(root.left, result)
      if root.right:
        traverse(root.right, result)
      result.append(root.value)
      return result
    return traverse(self.root)


      
class BinarySearchTree(BinaryTree):
  """Creates Instance of BinarySearchTree which Inherits from BinaryTree,
     Includes methods related to binary search 
  """
  def __init__(self):
    self.root = None
    
  def __str__(self):
    return f'BinarySearchTree Instance, root: {self.root}'

  def __repr__(self):
    return f'BinarySearchTree Instance, root: {self.root}'

  def contains(self, val):
    """Searches BinarySearchTree Instance for a node with a value equal to the argument `val`.
    """
    val = [val]
    def traverse(root, val):
      if not root:
        return
      if root.value == val[0]:
        val.append(True)
        return val
      if val[0] < root.value and root.left:
        traverse(root.left, val)
      if val[0] > root.value and root.right:
        traverse(root.right, val)
      
      val.append(False)
      return val

    return traverse(self.root, val)[1]

  def add(self, val):
      if not self.root:
        self.root = Node(val)
        return
      
      def traverse(root, val):
        if not root:
          return
        if root.value == val:
          raise ValueError(f'{val} already exists in BinarySearchTree')
        
        if val < root.value:
          if root.left == None:
            root.left = Node(val)
            return
          else:
            traverse(root.left, val)
        if val > root.value:
          if root.right == None:
            root.right = Node(val)
            return
          else:
            traverse(root.right, val)
          
      traverse(self.root, val)
      return
    
    

      
  
    
        
