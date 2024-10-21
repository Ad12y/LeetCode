class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1,2]
        if n == 1:
            return 1
        i = 2
        while i < n:
            lst.append(lst[i-1] + lst[i-2])
            i += 1 
        return lst[-1]
        