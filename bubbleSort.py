# Sorts a sequence in ascending order using the bubble sort algorithm
# worst case: O(n^2)
# best case :omega(n)
def bubbleSort(nums):
  n = len(nums)
  # Perform n-1 bubble operations on the sequence
  for i in range(0,n):
    # Bubble the largest item to the end
    for j in range(0,n-i-1):
      if nums[j] > nums[j+1]: #swap the j and j+1 items
        tmp = nums[j] 
        nums[j] = nums[j+1]
        nums[j+1] = tmp
  return nums

print bubbleSort([1,2,3,0])

def bubbleSort_improve(nums):
  count = -1 
  i = 0
  while count!=0:
    count = 0
    for j in range(0,len(nums)-1-i):
      if nums[j]>nums[j+1]:
        tmp = nums[j+1]
        nums[j+1] = nums[j]
        nums[j]=tmp
        count+=1
    i+=1
  return nums
print bubbleSort_improve([1,2,3,0])
