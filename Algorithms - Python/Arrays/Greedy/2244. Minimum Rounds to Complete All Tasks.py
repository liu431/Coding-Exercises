class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        from collections import Counter
        rounds = 0
        dic = Counter(tasks)
        for val in dic.values():
            if val == 1:
                return -1
            else:
                rounds += (val + 2) // 3
        return rounds
