class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert int to string
        s = str(x)
        # All negative numbers are excluded because of the "-" sign 
        if x < 0:
            return False
        else:
            for i in range(len(s)):
                # Compare the digits from both beginning and end
                if s[i] != s[-i-1]:
                    return False
            return True
