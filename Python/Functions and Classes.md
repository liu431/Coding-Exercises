## Functions

### Recursion
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
