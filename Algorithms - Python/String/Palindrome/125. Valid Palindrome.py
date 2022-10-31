class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert all uppercase letters into lowercase letters and remove all non-alphanumeric characters
        s = [i.lower() for i in s if i.isalnum()]
        # method 1: test whether it is valid palindrome
        return s == s[::-1]
        # method2: two pointers
        s_len = int(len(s))
        for ind in range(int(s_len/2)):
            if s[ind] != s[s_len - 1 - ind]:
                return False
        return True        
