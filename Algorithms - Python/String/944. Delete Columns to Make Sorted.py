class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cts = 0
        for i in range(len(strs[0])):
            col = [s[i] for s in strs]
            if ''.join(col) != ''.join(sorted(col)):
                cts += 1
        return cts
