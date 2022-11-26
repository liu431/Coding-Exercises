class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            current = nums[i]
            if current < nums[i - 1]:
                # insert at the start of nums
                if current == 0:
                    index = 0
                # insert right before the first 2
                elif current == 1:
                    index = nums.index(2) 
                else:
                    pass
                nums.insert(index, current)
                nums.pop(i + 1)
