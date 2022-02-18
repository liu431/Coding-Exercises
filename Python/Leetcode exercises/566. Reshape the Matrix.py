class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        else:
            # Convert to 1-d array
            mat1d = [0] * (m * n)
            for i in range(m):
                for j in range(n):
                    mat1d[n * i + j] = mat[i][j]
            # Convert to r*c array
            matrc = [[0] * c] * r
            for i in range(r * c):
                print(i//c, i%c, mat1d[i])
                matrc[i // c][i % c] = int(mat1d[i])
                print(matrc)
            return matrc
        
        
         
