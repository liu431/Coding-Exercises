class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = collections.Counter(str(n))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))
