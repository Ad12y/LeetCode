class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        min_val = float("inf") 

        if len(nums) == 1:
            return nums[0]

        while l<=r:
            mid = (l+r)//2
            min_val = min(min_val, nums[mid])
            min_val = min(min_val, nums[l])
            min_val = min(min_val, nums[r])
            print(mid)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return min_val
        