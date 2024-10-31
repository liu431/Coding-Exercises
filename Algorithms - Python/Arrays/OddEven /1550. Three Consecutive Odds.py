class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr = ''.join([str(i%2) for i in arr])
        return '111' in arr
