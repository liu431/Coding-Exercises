class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)
        res = 0
        for i in range(dim):
            # primary diagonal
            res += mat[i][i]
            # secondary diagonal
            if i != dim - i - 1:
                res += mat[i][dim - i - 1]

        return res

    
