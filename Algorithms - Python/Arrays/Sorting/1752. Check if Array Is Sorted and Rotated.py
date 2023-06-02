class Solution:
    def check(self, nums: List[int]) -> bool:
        # try different rotation positions
        for x in range(len(nums)):
            new_nums = nums[x:] + nums[:x]
            # check if the new array is sorted in non-decreasing order
            if new_nums == sorted(new_nums):
                return True
        return False
