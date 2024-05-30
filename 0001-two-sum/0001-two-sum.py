class Solution(object):
    def twoSum(self, nums, target):

        dic = {nums[0]:0}
        for i in range(1, len(nums)):
            if target - nums[i] in dic.keys():
                return [dic[target - nums[i]],i]
            else:
                dic[nums[i]] = i



        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        