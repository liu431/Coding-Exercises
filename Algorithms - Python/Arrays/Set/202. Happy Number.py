class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squares = set()
        while n not in sum_squares:
            sum_squares.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
