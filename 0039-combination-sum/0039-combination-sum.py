class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.ans = [] 
        def backtrack(lst, i, total):
            if total > target or i > len(nums)-1:
                return
            total += nums[i]
            lst.append(nums[i])
            if total == target:
                self.ans.append(lst[:])
            backtrack(lst, i, total)
            for j in range(i+1, len(nums)):
                backtrack(lst, j, total)
            lst.pop()

        for i in range(0, len(nums)):
            backtrack([], i, 0)
        print(self.ans)
        return self.ans
        