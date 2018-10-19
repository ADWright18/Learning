class Tree:
  def __init__(self, cargo, left=None, right=None):
    self.cargo = cargo
    self.left = left
    self.right = right

  def __str___(self):
    return str(self.cargo)

# Preorder traversal - the contents of root appears before the contents of
# the children
def preorderTraversal(tree):
  if (tree is None):
    return

  print(tree.cargo, end=" ")
  preorderTraversal(tree.left)
  preorderTraversal(tree.right)

# Postorder traversal - the contents of children appears before the contents of
# the root
def postorderTraversal(tree):
  if (tree is None):
    return

  postorderTraversal(tree.left)
  postorderTraversal(tree.right)
  print(tree.cargo, end=" ")

# Inorder traversal - the contents appear in the following order: left, root, right
def inorderTraversal(tree):
  if (tree is None):
    return

  inorderTraversal(tree.left)
  print(tree.cargo, end=" ")
  inorderTraversal(tree.right)

# Main Program
tree = Tree(1, Tree(2), Tree(5))

preorderTraversal(tree)
print("\n")
postorderTraversal(tree)
print("\n")
inorderTraversal(tree)
