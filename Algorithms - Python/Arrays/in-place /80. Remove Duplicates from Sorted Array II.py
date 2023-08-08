class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_cts = 0
        i = 2
        while i < len(nums):
            if nums[i] != '_':
                if nums[i] == nums[i - 1] == nums[i - 2]:
                    nums.remove(nums[i])
                    nums.append('_')
                    dup_cts += 1
                    i -= 1
            i += 1
        return len(nums) - dup_cts
