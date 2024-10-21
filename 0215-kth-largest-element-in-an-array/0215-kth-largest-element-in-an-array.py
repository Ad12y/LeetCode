class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        dic = {}
        for i in range(0, len(nums)):
            if -nums[i] not in dic:
                heapq.heappush(heap, -nums[i])
            if -nums[i] in dic:
                dic[-nums[i]].append(i)   
            else:
                dic[-nums[i]] = [i]
        print(dic)
        i = 0
        lst = []
        print(heap)
        while i < k:
            j = 0 
            pp = heapq.heappop(heap)
            print(pp)
            val = dic[pp]
            while i + j < k and j < len(val):
                lst.append(pp)
                j += 1
            i += j 
        print(lst)
        return -lst[-1]
        