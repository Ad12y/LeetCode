class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        heap = []

        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        print(dic)
        distinct = len(dic)
        idle_count = 0 
        count = 0
        last = 0
        for i in dic:
            heapq.heappush(heap, -dic[i])
        
        while heap:
            max_val = -heapq.heappop(heap)
            if n+1-distinct > 0 and (max_val - last):
                idle_count = n+1-distinct
            temp = (max_val - last)*(distinct + idle_count)
            print(temp)
            count += temp
            distinct -= 1
            last = max_val
        
        return count - idle_count