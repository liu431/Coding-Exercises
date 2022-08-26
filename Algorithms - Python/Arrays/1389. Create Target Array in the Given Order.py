class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, ind in enumerate(index):
            target.insert(ind, nums[i])
        return target
