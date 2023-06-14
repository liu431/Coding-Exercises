class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cts = 0
        # get dimensions
        rows, columns = len(grid), len(grid[0])
        # loop through the last row as they will be smallest
        for n in range(0, columns):
            for m in range(rows - 1, -1, -1):
                if grid[m][n] >= 0:
                    break
                else:
                    cts += 1
        return cts
