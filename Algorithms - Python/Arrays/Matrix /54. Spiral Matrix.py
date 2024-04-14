class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        while matrix:
            # left
            res += matrix.pop(0)
            # downard
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            # left
            if matrix:
                res += matrix.pop()[::-1]
            # upward
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    res.append(row.pop(0))
        return res
