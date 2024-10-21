import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return math.sqrt(x**2 + y**2)
        
        heap = []
        dist_dic = {}
        for point in points:
            dist_val = dist(point[0], point[1])
            heapq.heappush(heap, dist_val)
            if dist_val in dist_dic:
                dist_dic[dist_val].append(point)
            else:
                dist_dic[dist_val] = [point]
        print(dist_dic)
        i = 0
        lst = []
        while i < k:
            j = 0
            val = dist_dic[heapq.heappop(heap)]
            while i + j < k and j < len(val):
                lst.append(val[j])
                j += 1

            i += j


        
        return lst
        

        