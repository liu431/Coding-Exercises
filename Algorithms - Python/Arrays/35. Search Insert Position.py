class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''Find the position of a target value within a sorted array'''
        def binarysearch(low, high):
            mid = (low + high) // 2
            # Find exact match
            if nums[mid] == target:
                return mid
            # Find match to insert
            elif nums[mid] < target and nums[mid+1] > target:
                return mid + 1
            # Search on the left
            elif nums[mid] > target:
                return binarysearch(low, mid - 1)
            # Search on the right
            else:
                return binarysearch(mid + 1, high)
        # Edge case: target smaller than the smallest num in nums
        if target <= nums[0]:
            return 0
        # Edge case: target larger than the largest num in nums
        elif target > nums[-1]:
            return len(nums)
        # Call the binary function
        else:
            return binarysearch(0, len(nums)-1)
        
