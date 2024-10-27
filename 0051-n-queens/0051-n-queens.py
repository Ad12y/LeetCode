class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def check(row, col, queens_set):
            if any(r == row for r, c in queens_set) or any(c == col for r, c in queens_set):
                return False
            for queen_row, queen_col in queens_set:
                if abs(row - queen_row) == abs(col - queen_col):
                    return False
            return True
        def recur(i,j, set_):
            if len(set_) == n:
                self.ans.append(set_.copy())

            if i>n-1 or j>n-1:
                return False
            for j in range(0, n):
                if check(i, j, set_):
                    set_.add((i,j))
                    recur(i+1, j, set_)
                    set_.remove((i, j))
            return
        recur(0,0,set())

        for i in self.ans:
            res = [['.' for _ in range(n)] for _ in range(n)]  # Create a 2D list of '.'
            for j in i:
                row, col = j[0], j[1]
                res[row][col] = 'Q'
            for row in res:
                print(''.join(row))  # Join each row to create the string representation



                
            

            
