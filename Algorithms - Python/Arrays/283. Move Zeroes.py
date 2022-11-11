class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(i)

        # method 2        
        i = 0
        k =  len(nums)
        while i < k:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                k -= 1
            else:
                i += 1
