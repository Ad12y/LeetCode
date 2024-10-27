class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def recur(i, j, sum_, set_):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0 or (i,j) in set_:
                return 0
            set_.add((i,j))
            a = recur(i+1, j, sum_+1, set_)
            b = recur(i, j+1, sum_+1, set_)
            c = recur(i-1, j, sum_+1, set_)
            d = recur(i, j-1, sum_+1, set_)
            return 1 + a + b + c + d
        # print(recur(3, 8, 0, set()))

        ans = 0
        set_ = set()
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] and grid[i][j] not in set_:
                    ans = max(ans, recur(i,j, 0, set_))
        return ans