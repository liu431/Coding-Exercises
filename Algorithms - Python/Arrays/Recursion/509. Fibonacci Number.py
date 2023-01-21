class Solution:
    def fib(self, n: int) -> int:
        # initialize the result store
        res = 0
        # define the base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # recursion
        # Ex. f(4) = f(3) + f(2) = f(2) + f(1) + f(1) + f(0) = f(1) + f(0)+ f(1) + f(1) + f(0) = 1 + 0 + 1 + 1 + 0 = 3
        else:
            return self.fib(n-1) + self.fib(n-2)
