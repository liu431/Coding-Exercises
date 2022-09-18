class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = []
        for i in s.replace("01","0 1").replace("10","1 0").split():
            l.append(len(i))
        return sum(min(a,b) for a,b in zip(l,l[1:]))
