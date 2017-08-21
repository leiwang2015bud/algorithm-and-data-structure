from array import Array

class LinkedList:
  def __init__(self,maxsize):
    self._head =  _LinkedList("head",None)
    self._head.next =  _LinkedList("tail",None)
    self._count = 0

  def getResult(self):
    return self._head

  # search the target key in the sub list with the head
  def _search(self,head,target):
    if head.key == target or head.next.next is None: 
      return head
    return self._search(head.next,target)

  def add(self,target,key,value):
    head = self._search(self._head,target)
    if target == key :
      head.value = value
      return False
    else:
      print "---",value
      print head.key
      tmp = head.next
      head.next = _LinkedList(key,value)
      head.next.next = tmp
      self._count +=1


class _LinkedList:
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.next = None


