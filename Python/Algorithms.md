
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
