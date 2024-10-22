class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = [] 
        nums.sort()
        def recur(lst, i):
            if i > len(nums) - 1:
                self.ans.append(lst[:])
                return 
            lst.append(nums[i])
            recur(lst, i+1)
            lst.pop()
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i += 1 
            recur(lst, i+1)
            return

        recur([], 0)
        return self.ans

        