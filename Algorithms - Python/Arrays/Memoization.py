class Solution:
    def tribonacci(self, n: int) -> int:
        # Normal approach (Time Limit Exceeded)
        # res = 0
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 1
        # else:
        #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        # initial first 3 numbers
        a, b, c = 0, 1, 1
        # iteratively, use a,b,c to keep track of the latest 3 numbers
        for i in range(n):
            a, b, c = b, c, a + b+ c
        return a
