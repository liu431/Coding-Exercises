class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_row, n_col = len(matrix), len(matrix[0])
        for i in range(1, n_row):
            for j in range(1, n_col):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
