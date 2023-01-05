class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arr = 0
        y = float('inf')
        for start, end in sorted(points, reverse=True):
            if y > end:
                y = start
                arr += 1
        return arr
