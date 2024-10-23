class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def recur(i, j , k, set_):
            if i < 0 or i > len(board)-1:
                return False
            elif j < 0 or j > len(board[0])-1:
                return False
            elif (i,j) in set_:
                return False
            elif board[i][j] != word[k]:
                return False
            elif k == len(word)-1:
                return True
            set_.add((i,j))
            a = recur(i+1, j, k+1, set_)
            b = recur(i, j+1, k+1, set_)
            c = recur(i-1, j, k+1, set_)
            d = recur(i, j-1, k+1, set_) 
            set_.remove((i,j))
            return a or b or c or d

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if recur(i,j,0, set()):
                    return True
        return False




        