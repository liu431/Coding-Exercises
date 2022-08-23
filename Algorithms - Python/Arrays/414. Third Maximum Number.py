class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # should not use sort() as it is O(nlogn)
        nums = set(nums)
        maxN = max(nums)
        if len(nums) < 3:
            return maxN
        else:
            # remove the two largest num
            nums.remove(maxN)
            nums.remove(max(nums))
            return max(nums)
