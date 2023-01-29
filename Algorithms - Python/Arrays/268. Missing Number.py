class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        snums = sorted(nums)
        for ind, num in enumerate(snums):
            # When a number in [0,n) is missing
            if ind != snums[ind]:
                return ind
        # When n is missing
        return len(nums)
        

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)]
        return [i for i in arr if i not in nums][0]
