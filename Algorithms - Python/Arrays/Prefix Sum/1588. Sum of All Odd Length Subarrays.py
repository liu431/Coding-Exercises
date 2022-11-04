class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        interval = [i for i in range(1, len(arr) + 1) if i % 2 == 1]
        for k in interval:
            sub = [sum(arr[i:i+k]) for i in range(0, len(arr) - k + 1)]
            res += sum(sub)
        return res
