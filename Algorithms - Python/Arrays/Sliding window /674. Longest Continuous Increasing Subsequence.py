# for loop and updat ethe max subsequence length
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxL = 1
        L = 1
        for i in range(1, len(nums)):
            print(nums[i], nums[i - 1])
            if nums[i] > nums[i - 1]:
                L += 1
            else:
                # reset when followed by a non-increased number
                maxL = max(maxL, L)
                L = 1
            # case when array is all increasing
            maxL = max(maxL, L)
        return maxL
