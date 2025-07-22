class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            dic[nums[i]] = i
        
        for i in range(0, len(nums)):
            if target - nums[i] in dic.keys() and dic[target - nums[i]] != i:
                return [i,dic[target - nums[i]]] 
