class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Initialize result var
        res = []
        # Sort input arrays
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        # Find intersections by looping through element in the shorter array and see if it exists in the longer array
        ## When num2 is longer
        if len(n1) < len(n2):
            for i in n1:
                if i in n2:
                    res.append(i)
                    n2.remove(i)
        ## When num1 is longer
        else:
            for i in n2:
                if i in n1:
                    res.append(i)
                    n1.remove(i)
        return res
