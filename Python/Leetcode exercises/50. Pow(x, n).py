class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Take the fraction when n is negative
        if n < 0:
            x = 1 / x
            n = -n
        # Initialize the result when n is 0
        res = 1
        while n > 0:
            # Take square if n is even
            if (n % 2) == 0:
                x = x * x
                n = n // 2
            # Multiply the base
            else:
                res = res * x
                n -= 1
        return res
