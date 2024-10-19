class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li = []
        self.k = k
        i = 0
        if len(nums):
            while i in range(0, len(nums)):
                if i < k:
                    heapq.heappush(self.li, nums[i])
                else:
                    heapq.heappush(self.li, max(nums[i], heapq.heappop(self.li)))
                i += 1
            print(self.li)

    def add(self, val: int) -> int:
        if len(self.li) and len(self.li) >= self.k:
            heapq.heappush(self.li, max(val, heapq.heappop(self.li)))
        else:
            heapq.heappush(self.li, val)


        return self.li[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)