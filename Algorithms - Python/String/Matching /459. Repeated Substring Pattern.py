class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # brute foce: only work in simple cases
        # for i in range(1, len(s)):
        #     sub = s[:i]
        #     s_split = s.split(sub)
        #     print(s_split)
        #     if max([len(t) for t in s_split]) == 0:
        #         return True
        # return False

        return s in f"{s[1:]}{s[:-1]}"
