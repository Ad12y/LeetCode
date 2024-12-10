class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cal(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        matrix = [[0]*n for i in range(n)]
        # adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    matrix[i][j] = cal(points[i],points[j])
                    matrix[j][i] = matrix[i][j]
        # for (u, v) in points:
        #     adj[u].append(cal(u, v), j)
        print(matrix)

        visited = set()
        visited.add(0)
        heap = []
        heapify(heap) 
        for i in range(1,n):
            heappush(heap, (matrix[0][i], i)) 
        print(heap)
        dis = 0
        while heap and len(visited) != n:
            element = heappop(heap)
            p = element[1]
            if p in visited:
                continue
            dis += element[0]
            visited.add(p)
            for i in range(n):
                if i not in visited:
                    heappush(heap, (matrix[p][i], i)) 
        return dis








        