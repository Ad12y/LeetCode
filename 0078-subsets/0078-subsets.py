class Solution(object):
    def subsets(self, nums):
        stack = []
        res = []
        n = len(nums)
        def recur(i):
            if i >= n:
                res.append(stack[:])
                return

            stack.append(nums[i])
            recur(i+1)

            stack.pop()
            recur(i+1)
            return 

        recur(0)
        return res
            


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        