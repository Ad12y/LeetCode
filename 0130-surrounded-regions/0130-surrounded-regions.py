class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m, n = len(board)-1, len(board[0])-1  
        def dfs(i, j):
            if i > m or j > n:
                return 
            if i < 0 or j < 0:
                return 
            if board[i][j] == "X":
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)


        for i in [0, m]:
            for j in range(n+1):
                dfs(i, j)
        
        for i in range(m+1):
            for j in [0, n]:
                dfs(i,j)

        for i in range(m+1):
            for j in range(n+1):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"

            



        