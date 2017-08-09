# worst-cases: O(n^2)
# best-cases: O(n^2)
def selectionSort(nums):
  for j in range(0,len(nums)-1):# j is first index for unsorted sub array
    minimum = nums[j] # define the first elemnt in each unsorted sub array as minimum
    minimum_index = j
    for i in range(j,len(nums)-1):# i is the index of each elements for unsorted sub array
        if (minimum>nums[i+1]):
          minimum=nums[i+1]
          minimum_index = i+1
    nums[minimum_index] = nums[j]
    nums[j] = minimum
  return nums

print selectionSort([3,2,5,1])
