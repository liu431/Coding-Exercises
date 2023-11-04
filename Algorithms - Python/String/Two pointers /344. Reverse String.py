class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # two pointers are used to process two array elements at the same time 
        left, right = 0, len(s) -1 
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
