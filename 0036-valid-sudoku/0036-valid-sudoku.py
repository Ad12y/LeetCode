class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row_col(board):
            for i in range(0,9):
                lst_row = []
                lst_col = []
                for j in range(0,9):
                    if board[i][j] != ".":
                        lst_row.append(board[i][j]) 
                    if board[j][i] != ".":
                        lst_col.append(board[j][i])
                if len(set(lst_row)) != len(lst_row):
                    return False
                if len(set(lst_col)) != len(lst_col):
                    return False
            return True
        def check_grid(s):
            lst = []
            for i in range(s[0], s[0]+3):
                for j in range(s[1], s[1]+3):
                    if board[i][j] != ".":
                        lst.append(board[i][j]) 
            if len(set(lst)) == len(lst):
                return True 
            return False

        lst = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i in lst:
            if not check_grid(i):
                return False

        return check_row_col(board)
