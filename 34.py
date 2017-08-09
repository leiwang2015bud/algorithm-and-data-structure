class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1] 
        start = self.binary_search(nums,target-0.5)
        print start
        if nums[start]!=target:
        	return [-1,-1]
        nums.append(0)
        end = self.binary_search(nums,target+0.5)-1
        return [start,end]

    def binary_search(self,nums,target):
    	start,end = 0, len(nums)-1
    	while start != end:
    		mid = (start+end)/2
    		if target <nums[mid]:
    			end = mid-1
    		else:
    			start = mid+1
    	return start

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if len(nums)==0:
			return [-1,-1]
		i = self.binary_search(nums,target-0.5)
		j = self.binary_search(nums,target+0.5)
		if nums[start]!=target:
			return [-1,-1]
		elif nums[end]!=target:
			j = j -1
			return [i,j]

	def binary_search(self,nums,target):
		i,j = 0, len(nums)-1
		while i < j:
			mid = (i+j)/2
			if target < nums[mid]:
				j = mid
			else: # nums[mid]<target or nums[mid]==target
				i = mid+1
		return i

class Solution3(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [-1,-1]
        if len(nums)==0:
            return index
        i,j = 0,len(nums)-1
        # Search for the left one
        while i<j:
        	mid = (i+j)/2
        	if nums[mid] < target:
        		i = mid +1
        	else:
        		j = mid
        if nums[i]!=target:
        	return index
        else:
        	index[0]=i
        # Search for the right one
        j =  len(nums)-1
        while i < j:
        	mid = (i+j)/2+1
        	if nums[mid] > target:
        		j = mid -1
        	else:
        		i = mid
        index[1] = j
        return index

print Solution2().searchRange([2,2],3)



