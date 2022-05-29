class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store key: target - num; value: index of searched value
        pair = {}
        for ind, num in enumerate(nums):
            # Not find the match
            if num not in pair:
                pair[target - num] = ind
            # Find the match
            else:
                return [pair[num], ind]
