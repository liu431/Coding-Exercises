class Solution:
    def mySqrt(self, x: int) -> int:
        # can use x*x
        previous = 0
        current = 0
        for i in range(0, x + 1):
            sqr = i * i
            if sqr < x:
                previous, current = current, sqr
            elif sqr == x:
                return i
            else:
                return i - 1

# x = 4
# for (1, 2, 3, 4, 5, 6, 7, 8)
# i = 1, sqr = 1 < 8 => previous = 0, current = 1
# i = 2, sqr = 4 < 8 => previous = 1, current = 4
# i = 3, sqr = 9 < 8 => return 3

# complexity: O(x)

