class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # get index of val in nums
        val_ind = [i for i, v in enumerate(nums) if v == val]
        # track num of val occurrence
        ct = 0
        # loop through nums and modify in place
        for i in val_ind:
            nums.pop(i - ct)
            nums.append('_')
            ct += 1
        return len(nums) - ct
