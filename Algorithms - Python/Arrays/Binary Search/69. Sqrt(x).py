class Solution:
    def mySqrt(self, x: int) -> int:
        
        def binary_search(low, high):

            mid = (low + high) // 2
            midsqr = mid * mid 
            if midsqr <= x and (mid+1) * (mid+1) > x :
                return mid
            elif midsqr > x:
                return binary_search(low, mid-1)
            else:
                return binary_search(mid+1, high)
        return binary_search (0, x)
