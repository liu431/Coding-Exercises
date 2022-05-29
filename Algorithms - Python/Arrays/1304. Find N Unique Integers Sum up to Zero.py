class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # when n is odd
        if n % 2 == 1:
            res.append(0)
            for i in range(1, int((n-1)/2)+1):
                res.append(i)
                res.append(-i)
        # when n is even
        else:             
            for i in range(1, int(n/2)+1):
                res.append(i)
                res.append(-i)
            
        return res
