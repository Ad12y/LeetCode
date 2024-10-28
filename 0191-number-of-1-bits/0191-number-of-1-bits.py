class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        count = 0 
        while num:
            count += num&1
            num = num>>1
        return count
        