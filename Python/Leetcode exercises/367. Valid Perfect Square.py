class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Program for recursive binary search
        def binary(low, high):
            if high >= low:
                # Take the middle number
                mid = (low + high) // 2
                # Get the square
                midsqr = mid ** 2
                # Evaluate values
                if midsqr == num:
                    return True
                elif midsqr > num:
                    # Take the left subarray 
                    return binary(low, mid - 1)
                else:
                    # Take the right subarray
                    return binary(mid + 1, high)
            # No match if high > low after several recursions
            else:
                return False
            
        # Call the recursive function
        return binary(1, num)
            
        
