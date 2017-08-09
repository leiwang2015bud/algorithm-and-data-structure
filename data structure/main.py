from classes.array import Array
from classes.maxheap import MaxHeap

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

theSeq = [5,3,6,8,1]
print theSeq
# """
## build the max heap, the output is the sorted array
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