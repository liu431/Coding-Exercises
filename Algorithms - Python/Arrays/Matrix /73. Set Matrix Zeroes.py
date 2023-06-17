class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_z, col_z = set(), set()
        row_n, col_n = len(matrix), len(matrix[0])

        # find row and column indicators that contain zero
        for i in range(row_n):
            for j in range(col_n):
                if matrix[i][j] == 0:
                    row_z.add(i)
                    col_z.add(j)
        
        # change to zero in place
        for i in range(row_n):
            for j in range(col_n):
                if i in row_z or j in col_z:
                    matrix[i][j] = 0
