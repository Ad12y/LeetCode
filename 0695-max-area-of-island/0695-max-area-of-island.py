class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def recur(i, j, visited):
            # Check bounds and validity
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0 or (i,j) in visited:
                return 0
                
            # Mark as visited
            visited.add((i,j))
            
            # Calculate area = 1 (current cell) + all adjacent cells
            area = 1 + (recur(i+1, j, visited) +  # down
                       recur(i-1, j, visited) +    # up
                       recur(i, j+1, visited) +    # right
                       recur(i, j-1, visited))     # left
            
            return area
        
        # Check each cell as a potential starting point
        max_area = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, recur(i, j, visited))
        
        return max_area