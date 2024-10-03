class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_length = 0
        j = 0 
        for i in range(0, len(nums)):
            if nums[i] - 1 not in num_set:
                j = 1
                while nums[i] + j in num_set:
                    j += 1
            max_length = max(max_length,j)

        return max_length

        