class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        for i in nums:
            try:
                dic[i] += 1
            except:
                dic[i] = 1

        mew = sorted(dic.items(), key = lambda x: x[1], reverse = True) 
        return [i[0] for i in mew][0:k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        