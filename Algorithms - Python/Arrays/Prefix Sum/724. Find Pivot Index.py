class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            # Remaining part is the total sum minus current sum and the pivot number
            right = total - left - n
            # Sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right
            if left == right:
                return i
            left += n
        return -1
        
