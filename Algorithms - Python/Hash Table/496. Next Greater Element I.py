class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2dic = {}
        for ind, n in enumerate(nums2):
            # find the first greater element that is to the right of x in the same array.
            next_greater = [i for i in nums2[ind + 1:] if i > n]
            if next_greater:
                n2dic[n] = next_greater[0]
            else:
                n2dic[n] = -1
                
        return [n2dic[i] for i in nums1]
            
