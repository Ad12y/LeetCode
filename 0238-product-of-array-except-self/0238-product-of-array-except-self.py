class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        z_c = 0
        j = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                j = i
                z_c += 1
            else:
                p *= nums[i]
        if z_c > 1:
            return [0]*len(nums)
        elif z_c == 1:
            return [p if i == 0 else 0 for i in nums]
        return [p/i for i in nums]  
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        