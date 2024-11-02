class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        a = {}
        for i in s:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        a_odd = [i for i, j in a.items() if j % 2 == 1]
        return len(a_odd) < 2
