import heapq as hq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dic = {}
        for i in range(0,len(points)):
            dic[i] = (points[i][0]**2 + points[i][1]**2)**(0.5)
            
        di = [(dic[i], points[i]) for i in dic.keys()]
        hq.heapify(di)
        lst = []
        for i in range(0,k):
            lst.append(list(heapq.heappop(di)[1]))
        return lst
