
## Recursion
A function that calls itself

Ex. [Leetcode 231. Power of Two](https://github.com/liu431/Technical-Skills/blob/master/Python/Leetcode%20exercises/231.%20Power%20of%20Two.py)

```python
def factorial(x):
    """Find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print(factorial(3)) # 6
```

Ex. Generate first N numbers in Fibonacci series
 ```python
def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst
```

### Binary search

Ex. [LC 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
```python
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
 ```        
