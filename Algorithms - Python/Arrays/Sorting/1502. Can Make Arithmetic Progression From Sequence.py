class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arrSorted = sorted(arr)
        diff = [arrSorted[i + 1] - arrSorted[i] for i in range(len(arr) - 1)]
        return len(set(diff)) == 1
