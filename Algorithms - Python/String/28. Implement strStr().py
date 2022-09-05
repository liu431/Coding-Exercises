class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Return 0 when needle is an empty string
        if needle == '':
            return 0
        for ind, s in enumerate(haystack):
            # First strings match
            if s == needle[0]:
                # Check if all letters match
                if needle == haystack[ind:len(needle)+ind]:
                    return ind
        # Needle is not part of haystack
        return -1
                
                
                    
        
