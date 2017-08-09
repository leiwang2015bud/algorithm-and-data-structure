class Solution(object):
  def search(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: bool
      """
      if len(nums)==0:
          return False
      if len(nums)==1:
          if target == nums[0]:
              return True
          else:
              return False
      i = 0
      j = len(nums)
      while(i!=j):
          if nums[j-1]< target and target <nums[i]:
              return False

          if target == nums[i]:
              return True
          if target == nums[j-1]:
              return True

          M = (i+j)/2
          if target == nums[M]:
              return True

          if nums[i]==nums[M]:
              if nums[i]<target and target<=nums[M-1]:
                  j = M
              else:
                  i = i+1
              
          elif nums[i]<nums[M]:
              if nums[i]<target and target<nums[M]:
                  j = M
              else:
                  i = M+1
          else:
              if nums[M]<target and target<nums[j-1]:
                  i = M+1
              else:
                  j = M
      return False

for i in range(1,4):
  print i

i = 4
while(i<4):
  print i
  i = i+1