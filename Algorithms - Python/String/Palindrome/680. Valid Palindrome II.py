class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_len = int(len(s))
        for ind in range(int(s_len/2)):
            if s[ind] != s[s_len - 1 - ind]:
                # remove occurence of the unmatched char from start
                s_left_drop = s[:ind] + s[ind + 1:]
                # remove occurence of the unmatched char from last
                s_right_drop = s[:s_len - 1 - ind] + s[s_len - ind:]
                return s_left_drop == s_left_drop[::-1] or s_right_drop == s_right_drop[::-1]
        return True        
