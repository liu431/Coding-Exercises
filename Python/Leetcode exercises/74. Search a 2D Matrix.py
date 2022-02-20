class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Recusive function for binary search
        def binary(matrix, target, low, high):
            if low > high:
                return False
            else:
                mid = (low + high) // 2
                # Target in the sublist
                if target in matrix[mid]:
                    return True
                # Move to the left side
                elif target < matrix[mid][0]:
                    return binary(matrix, target, low, mid - 1)
                # Move to the right side
                elif target > matrix[mid][-1]:
                    return binary(matrix, target, mid + 1, high)
                # Target not in the sublist with range that includes the target value 
                else:
                    return False
                
        # Edge cases: when target is outside the range 
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        # Run binary search
        return binary(matrix, target, 0, len(matrix))
                
        
