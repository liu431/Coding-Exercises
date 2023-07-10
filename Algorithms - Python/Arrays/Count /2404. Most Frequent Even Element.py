class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # only count the even element
        cts = {}
        for i in nums:
            if i % 2 == 0:
                if i in cts:
                    cts[i] += 1
                else:
                    cts[i] = 1
        # find the most frequent even element
        if len(cts) > 0:
            maxcts = max(cts.values())
            res = []
            for n in cts:
                if cts[n] == maxcts:
                    res.append(n)
            return min(res)
        else:
            return -1
