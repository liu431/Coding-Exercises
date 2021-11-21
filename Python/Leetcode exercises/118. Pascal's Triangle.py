class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        num = 3
        while num <= numRows+1:
            # All rows start and end with 1
            row = [1, 1]
            # Get the above row
            row_prev = res[-1]
            # Insert values based on the previous row values
            for i in range(1, num - 2):
                row.insert(i, row_prev[i-1]+row_prev[i])
            res.append(row)
            num += 1
            
        return res
        
