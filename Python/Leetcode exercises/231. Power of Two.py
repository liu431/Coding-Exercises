class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      # Given an integer n, return true if it is a power of two. Otherwise, return false
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            if n % 2 == 1:
                return False
            else:
                # Recursion
                return self.isPowerOfTwo(n / 2)
