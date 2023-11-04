class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        print(nums)
        for i in range(1, n):
            print(i)
            try:
                nums.remove(i)
            except:
                return False
        return len(nums) == 1 and nums[0] == n - 1
