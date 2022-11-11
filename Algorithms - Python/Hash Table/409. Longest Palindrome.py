class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dic = collections.Counter(s)
        lens = 0
        single_flag = 0
        for l, cts in s_dic.items():
            if cts % 2 == 0:
                lens += (2 * (cts // 2))
            elif cts > 1 and cts % 2 == 1:
                lens += (2 * (cts // 2))
                single_flag = 1
            else:
                single_flag = 1
        return lens + single_flag
