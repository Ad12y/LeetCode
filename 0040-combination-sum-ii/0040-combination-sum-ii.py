class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        def recur(lst, sum_, i):
            if sum_ > target or i > len(candidates)-1: 
                return sum_
            lst.append(candidates[i])
            sum_ += candidates[i] 
            if sum_ == target:
                if lst not in self.res:
                    self.res.append(lst[:])
            recur(lst, sum_, i+1)
            lst.pop()
            sum_ -= candidates[i] 
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1 
            for j in range(i+1, len(candidates)):
                if target >= recur(lst, sum_, j):
                    break
            return sum_
        for i in range(0, len(candidates)):
            recur([],0, i)
        return self.res