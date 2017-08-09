# the storage class for creating binary tree nodes
class _BinTreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

# first visit the node and then traverse both subtrees
def preorderTrav( subtree ):
  if subtree is not None:
    print( subtree.data )
    preorderTrav( subtree.left )
    preorderTrav( subtree.right )

def inorderTrav( subtree ):
  if subtree is not None:
    inorderTrav( subtree.left )
    print (subtree.data)
    inorderTrav( subtree.right)

def postorderTrav( subtree ):
  if subtree is not None:
    postorderTrav( subtree.left )
    postorderTrav( subtree.right )
    print( subtree.data)