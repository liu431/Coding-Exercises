class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # When n is non positive
        if n <= 0:
            return False
        # When n is positive
        while n != 1:
            # When n cannot be divided by 3
            if n % 3 != 0:
                return False
            # Iterate to n/3
            else:
                n /= 3
        return True
            
        
