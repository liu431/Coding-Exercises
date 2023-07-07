class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = ''.join([str(n) for n in nums]).split('0')
        return max([len(i) for i in ones])
