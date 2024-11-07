class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs():
            minutes = 0
            queue = []

            m, n = len(grid)-1, len(grid[0])-1
            for i in range(m+1):
                for j in range(n+1):
                    if grid[i][j] == 2:
                        queue.append((i,j, 0))

            while queue:
                temp = queue.pop()
                a = temp[0]
                b = temp[1] 
                c = temp[2]
                minutes = max(minutes, c)
                if a + 1 <= m and grid[a + 1][b] == 1:
                    queue.insert(0, (a+1, b, c+1))
                    grid[a + 1][b] = 2
                if b + 1 <= n and grid[a][b + 1] == 1:
                    queue.insert(0, (a, b+1, c+1))
                    grid[a][b + 1] = 2
                if a - 1 >= 0 and grid[a-1][b] == 1:
                    queue.insert(0, (a-1, b, c+1))
                    grid[a-1][b] = 2 
                if b - 1 >= 0 and grid[a][b-1] == 1:
                    queue.insert(0, (a, b-1, c+1))
                    grid[a][b-1] = 2
                    
            print(minutes)
            return minutes

                    
        val  = bfs()

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return val

    
    

        