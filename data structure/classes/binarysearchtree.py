from array import Array
class BSTMap:
  # Creates an empty map instance.
  def __init__(self):
    self._root = None
    self._size = 0

  # Returns the number of entries in the map.
  def __len__(self):
    return self._size

  # Returns an iterator for traversing the keys in the map.
  def __iter__(self):
    return _BSTMapIterator(self._root,self._size)

  # Determines if the map contains the given key
  def __contains__(self,key):
    return self._bstSearch(self._root,key) is not None

  # Returns the value associated with the key
  def valueOf(self, key):
    node = self._bstSearch(self._root, key)
    assert node is not None, "Invalid map key."
    return node.value

  # Helper method that recursively searches the tree for a target key
  def _bstSearch(self, subtree, target):
    # if subtree is None: # base case #lily modified
    #   return subtree
    # elif target < subtree.key: # target is left of the subtree root
    #   return self._bstSearch(subtree.left,target)
    # elif target > subtree.key: # target is right of the subtree root
    #   return self._bstSearch(subtree.right,target)
    # else:   # base case
    #   return subtree
    if subtree is None or subtree.key == target: # lily modified
      return subtree
    if target < subtree.key:
      return self._bstSearch(subtree.left, target)
    else:
      return self._bstSearch(subtree.right,target)

  def valueOfMin(self):
    node = self._root
    assert node is not None, "Empty BST"
    return self._bstMinimum(node).value

  def valueOfMax(self):
    node = self._root
    assert node is not None, "Empty BST"
    return self._bstMaximum(node).value

  # Helper method for finding the node caontaining the minimum key.
  def _bstMinimum(self, subtree):
    if subtree is None:
      return None
    elif subtree.left is None:
      return subtree
    else:
      return self._bstMinimum(subtree.left)

  # Helper method for finding the node caontaining the maximum key
  def _bstMaximum(self, subtree):
    if subtree is None:
      return None
    elif subtree.right is None:
      return subtree
    else:
      return self._bstMaximum(subtree.right)

  # Adds a new entry to the map or replaces the value of an existing key.
  def add(self, key, value):
    # Find the node containing the key, if it exists.
    node = self._bstSearch(self._root,key)
    # If the key is already in the tree, update its value.
    if node is not None:
      node.value = value
      return False
    # Otherwise, add a new entry.
    else:
      self._root = self._bstInsert(self._root, key, value)
      self._size +=1
      return True

  # Helper method that inserts a new item, recursively.
  def _bstInsert(self, subtree, key, value):
    if subtree is None:
      subtree = _BSTMapNode(key, value)
    elif key < subtree.key:
      subtree.left = self._bstInsert(subtree.left, key ,value)
      subtree.left.p = subtree
    elif key > subtree.key:
      subtree.right = self._bstInsert(subtree.right, key, value)
      subtree.right.p = subtree
    return subtree

  # Removes the map entry associated with the given key.
  def remove(self, key):
    assert key in self,"Invalid map key."
    self._root = self._bstRemove(self._root, key)
    self._size -= 1

  # Helper method that removes an existing item recursively.
  def _bstRemove(self, subtree, target):
    # # Search for the item in the tree
    # if subtree is None:
    #   return subtree
    # elif target < subtree.key:
    #   subtree.left = self._bstRemove(subtree.left, target)
    #   return subtree
    # elif target > subtree.key:
    #   subtree.right = self._bstRemove(subtree.right, target)
    #   return subtree
    # # we found the node containing the item.
    # else:
    #   if subtree.left is None and subtree.right is None:
    #     return None
    #   elif subtree.left is None or subtree.right is None:
    #     if subtree.left is not None:
    #       return subtree.left
    #     else:
    #       return subtree.right
    #   else:
    #     successor = self._bstMinimum(subtree.right)
    #     subtree.key = successor.key  #cover it 
    #     subtree.value = successor.value
    #     subtree.right = self._bstRemove(subtree.right, successor.key) # delete it
    #     return subtree
    z = self._bstSearch( subtree, target)
    if z.left == None:
      z.p = self._transPlant(z,z.right)
    elif z.right == None:
      z.p = self._transPlant(z,z.left)
    else:
      y = _successor()
      if y.p != x:
        y.p = self._transPlant(y,y.right)
        y.right = z.right
        y.right.p = y
      z.p = self._transPlant(z,y)
      y.left = z.left
      y.left.p = y
    return self._root


  def _successor(self,x):
    if x.right != None:
      return self._bstMinimum(x.right)
    y = x.p
    while(y!=None and x == y.right):
      x = y
      y = x.p
    return y

  def _transPlant(self,u,v):
    if u.p == None:
      self._root = v
    elif u == u.p.left:
      u.p.left = v
    else:
      u.p.right = v
    if v != None:
      u.p = v.p 
    return u.p

class _BSTMapNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
    self.p = None

class _BSTMapIterator:
  def __init__(self, root, size):
    # Creates the array and fills it with the keys
    self._theKeys = Array(size)
    self._curItem = 0 # Keep track of the next location in the array.
    self._bstTraversal(root)
    self._curItem = 0 # Reset the current item index.

  def __iter__(self):
    return self

  # Returns the next key from the array of keys
  def __next__(self):
    if self._curItem < len(self._theKeys):
      key = self._theKeys[self._curItem]
      self._curItem +=1
      return key
    else:
      raise StopIteration

  # Performs an inorder traversal used to build the array of keys.
  def _bstTraversal(self, subtree):
    if subtree is not None:
      self._bstTraversal(subtree.left)
      self._theKeys[self._curItem] = subtree.key
      self._curItem +=1
      self._bstTraversal(subtree.right)