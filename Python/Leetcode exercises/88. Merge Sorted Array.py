class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Get the values in nums1
        nums1_m = nums1[:m]
        # Initialize two pointers
        p1, p2 = 0, 0
        for p in range(n + m):
            # Use the val from nums1_m
            if (p1 < m and nums1_m[p1] <= nums2[p2]) or n <= p2:
                nums1[p] = nums1_m[p1]
                p1 += 1
            # Use the val from nums2
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        
