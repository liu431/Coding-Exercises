class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        n_col = len(matrix[0])
        for i in range(n_col):
            out.append([row[i] for row in matrix])
        return out
