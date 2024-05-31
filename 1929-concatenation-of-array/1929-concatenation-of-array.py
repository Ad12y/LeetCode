class Solution(object):
    def getConcatenation(self, nums):
        
        ans = [0]*2*len(nums)
        
        for i in range(0,len(ans)):
            ans[i] = nums[i%len(nums)]
        
        return ans
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        