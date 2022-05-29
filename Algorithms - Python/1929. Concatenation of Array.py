class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Build an array of size 2 * n
        n = len(nums)
        res = [0] * (2 * n)
        # Assign num[i] to ans[i] and ans[i + n]
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i + n] = nums[i]
        return res
        
