class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # optimize number of children who get th cookies -> greedy algorithm
        # two lists g and s -> two pointers
        child = 0
        cookie = 0
        g.sort()
        s.sort()
        while child < len(g) and cookie < len(s) and g[child] <= s[-1]:
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1

        return child
