# worst-cases: O(n^2)
# best-cases: O(nlgn)
class QuickSort:
  def __init__(self,nums):
    self._A = nums
    self._quickSort(0,len(nums)-1)

  def getResult(self):
    return self._A

  def _quickSort(self,p,r):
    if p < r:
      q = self._partition(p,r)
      self._quickSort(p,q-1)
      self._quickSort(q+1,r)

  def _partition(self,p,r):
    x = self._A[r]
    i = p-1
    for j in range(p,r):
      if self._A[j]<=x:
        i = i + 1
        tmp = self._A[i]
        self._A[i] = self._A[j]
        self._A[j] = tmp
    tmp = self._A[i+1]
    self._A[i+1] = x
    self._A[r] = tmp
    return i+1

nums = [3,2,5,1]
sort = QuickSort(nums)
print sort.getResult()



