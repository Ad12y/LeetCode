class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights[0]), len(heights[0])
        def dfs(val, i ,j, visited, res):
            if i<0 or j<0:
                res.add(1)
                if 1 in res and 2 in res:
                    return True
                return False
            elif i>m-1 or j>n-1:
                res.add(2)
                if 1 in res and 2 in res:
                    return True
                return False 
            if heights[i][j] > val or (i, j) in visited:
                return False
            val = heights[i][j]
            visited.add((i,j))
            a = dfs(val, i+1, j, visited, res)
            b = dfs(val, i, j+1, visited, res)
            c = dfs(val, i-1, j, visited, res)
            d = dfs(val, i, j-1, visited, res)
            return a or b or c or d
        
        res = []
        for i in range(m):
            for j in range(n):
                if dfs(heights[i][j], i, j, set(), set()):
                    res.append([i,j])
        return res

        