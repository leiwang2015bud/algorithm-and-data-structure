from classes.array import Array
from classes.maxheap import MaxHeap

############################################# heapsort with MaxHeap data structure
def simpleHeapSort(theSeq):
  #Create an array-based max-heap.
  n = len(theSeq)
  heap = MaxHeap(n)
  # Build a max-heap from the list of values.
  for item in theSeq:
    heap.add(item)
  # Extract each value from the heap and store them back into the list.
  for i in range(n-1,-1,-1): # modified by leiwang
    theSeq[i] = heap.extract()
  return theSeq

# Sorts a sequence in ascending order using the heapsort.
def heapsort(theSeq):
  n = len(theSeq)
  # Build a max-heap within the same array.
  for i in range(n):
    siftUp(theSeq, i)

  # Extract each value and rebuild the heap.
  for j in range(n-1,0,-1):
    tmp = theSeq[j]
    theSeq[j] = theSeq[0]
    theSeq[0] = tmp
    siftDown(theSeq, j-1, 0)

def buildHeap(theSeq):
  n = len(theSeq)
  heap = MaxHeap(n)
  for item in theSeq:
    heap.add(item)
  return heap

################################################## more efficient heapsort

class HeapSort():
  def __init__(self, A):
    self._A = A
    self._heapSize = 0

  def getSortedResult(self):
    return self._A

  def _left(self,i):
    return 2 * i + 1

  def _right(self,i):
    return 2 * i + 2

  def _max_heapify(self,i):
    l = self._left(i)
    r = self._right(i)
    if l < self._heapSize and self._A[l] > self._A[i]:
      largest = l
    else:
      largest = i
    if r < self._heapSize and self._A[r] > self._A[largest]:
      largest = r
    if largest != i:
      tmp = self._A[i]
      self._A[i] = self._A[largest]
      self._A[largest] = tmp
      self._max_heapify(largest)

  def _build_max_heap(self):
    self._heapSize = len(self._A)
    n = int((self._heapSize-1)/2)
    for i in range(n,-1,-1):
      self._max_heapify(i)

  def doIt(self):
    self._build_max_heap()
    n = self._heapSize-1
    for i in range(n,0,-1):
      tmp = self._A[0]
      self._A[0] = self._A[i]
      self._A[i] = tmp
      self._heapSize -= 1
      self._max_heapify(0)
import time

theSeq = [5,3,6,8,1,10,4,38,4,7,9]
print theSeq
# """
## build the max heap, the output is the sorted array
start_time = time.time()
h = buildHeap(theSeq)
# Test for heap building
a = h._getHeap()
a_it = a.__iter__().__iter__()
try:
  while True:
    print a_it.__next__()
except StopIteration:
  pass
# """
print simpleHeapSort(theSeq)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
hs = HeapSort(theSeq)
hs.doIt()
print hs.getSortedResult()
print("--- %s seconds ---" % (time.time() - start_time))