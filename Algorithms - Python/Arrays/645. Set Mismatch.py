class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Output: [number that occurs twice, the number that is missing]
        sum_set = sum(set(nums))
        return [sum(nums) - sum_set, sum(range(1, len(nums)+1)) - sum_set]
