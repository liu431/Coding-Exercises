class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        # Euclidean Algorithm
        while b:
            a, b = b, a%b
        return a
