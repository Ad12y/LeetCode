class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recur(lst, i):
            if i > len(nums) - 1:
                self.ans.append(lst[:])
                return 
            lst.append(nums[i])
            recur(lst, i+1)
            lst.pop()
            recur(lst, i+1)
            return
        recur([], 0)
        return self.ans


        