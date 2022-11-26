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

                
# re-construct teh arry with counts
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        m0 = nums.count(0)
        m1 = m0 + nums.count(1)
        m2 = m1 + nums.count(2)
        j = 0
        while(j < len(nums)):
            if j < m0:
                nums[j] = 0
            elif j < m1:
                nums[j] = 1
            elif j < m2:
                nums[j] = 2
            j += 1
        return nums
