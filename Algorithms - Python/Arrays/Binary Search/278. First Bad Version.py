# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def search(low, high):
            mid = (low + high) // 2
            check = isBadVersion(mid)
            check_before = isBadVersion(mid - 1)
            if check == 1 and check_before == 0:
                return mid
            elif check == 1 and check_before == 1:
                return search(low, mid - 1)
            else:
                return search(mid + 1, high)
        return search(1, n)
