class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = nums[0]
        j = nums[0]
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break 

        i = nums[0]
        while i!=j:
            i = nums[i]
            j = nums[j]

        return i


        