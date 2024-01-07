# it is a multiple of 5 and an even number that leads to a trailing zero 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n >= 5:
            n = n // 5
            cnt += n
        return cnt
