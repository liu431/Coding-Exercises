class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" #keep track of current max palindromic substring
        self.len = len(s)
        for i in range(self.len):
            # odd case, like "aba"
            odd = self.getPalindrom(s, i, i)
            # even case, like "abba"
            even = self.getPalindrom(s, i, i+1)
            # update the current max palindromic substring
            res = max(res, odd, even, key=len)
        return res
        
    # get the longest palindrome by trying to expand outwards
    # l, r are the middle indexes from inner to outer    
    def getPalindrom(self, s, l, r):
        while l >= 0 and r < self.len and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
