class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j, visited):
            if i>m-1 or j>n-1:
                return 0
            elif i<0 or j<0 or (i, j) in visited or grid[i][j]=="0":
                return 0
            visited.add((i,j))
            dfs(i+1,j, visited)
            dfs(i,j+1, visited)
            dfs(i-1,j, visited)
            dfs(i,j-1, visited)
            return 1
        visited = set()
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and grid[i][j] not in visited:
                    res += dfs(i,j,visited)

        return res
        