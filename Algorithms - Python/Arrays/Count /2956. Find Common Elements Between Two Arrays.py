class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1l = [i for i in nums1 if i in nums2]
        a2l = [i for i in nums2 if i in nums1]
        return [len(a1l), len(a2l)]
