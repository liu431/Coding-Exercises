class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSub, maxSub = nums[0], nums[0]
        # Iterate through the input
        for n in nums[1:]:
            # Add numbers to the current subarray
            # Reset the array if sum of subarray is negative
            currSub = max(n, currSub + n)
            # Update it whenever we find a bigger subarray
            maxSub = max(maxSub, currSub)
        return maxSub
        
        
