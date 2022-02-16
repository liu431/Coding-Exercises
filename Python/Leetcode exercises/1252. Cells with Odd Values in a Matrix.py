class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize the array
        x, y = [0]*m, [0]*n
        # Increment
        for r, c in indices:
            x[r] += 1
            y[c] += 1
        # Count odd numbers
        return sum([(i+j)%2 for i in x for j in y])
    
