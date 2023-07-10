class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        comm = [i for i in nums1 if i in nums2]
        answer = []
        answer.append([i for i in nums1 if i not in comm])
        answer.append([i for i in nums2 if i not in comm])
        return answer

