import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in range(0,len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        # heap = [(-v, k) for k, v in dic.items()]
        heap = []
        print(dic)

        for key, val in dic.items():
            heapq.heappush(heap,(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
                

        