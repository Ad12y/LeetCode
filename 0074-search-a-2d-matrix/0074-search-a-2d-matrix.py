class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m):
            print(matrix[i][0],matrix[i][n-1])
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                print("sds")
                if target == matrix[i][0]:
                    return True
                if target == matrix[i][n-1]:
                    return True

                print(1, n-1)
                for j in range(1, n-1):
                    print(i, j)
                    if matrix[i][j] == target:
                        return True
        return False



