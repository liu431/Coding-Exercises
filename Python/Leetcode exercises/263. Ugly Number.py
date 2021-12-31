class Solution:
    def isUgly(self, n: int) -> bool:
        # Edge case when n = 0
        if n == 0:
            return False
        
        # Get the final prime factors after dividing 2,3,5 while it can
        for p in 2, 3, 5:
            while n % p == 0:
                n = int(n / p)
                
        # If the reminding factor is not 2,3,5, return False
        # if the reminfing factor is 1, return True
        return n == 1
        
        
        
