class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {i: False for i in nums}
        longest = 0
        for i in nums:
            if d.get(i): 
                continue
            length = 1
            d[i]=True
            j = i+1
            while d.get(j) is not None:
                d[j]=True 
                length = length +1
                j +=1
            j = i-1
            while d.get(j) is not None:
                d[j]=True
                length = length +1
                j -=1
            longest = max(longest,length)
        return longest

print Solution().longestConsecutive([100,4,200,1,3,2])