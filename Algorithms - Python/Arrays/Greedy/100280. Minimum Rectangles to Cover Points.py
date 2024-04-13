class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        # get the sorted x, then segment by within x with greedy
        x_s = sorted([i[0] for i in points])
        num = 0
        index = 1
        n = len(x_s)
        i = 0
        while i < n:
            num += 1
            x_start = x_s[i]
            x_end = x_start + w
            
            while i < n and x_s[i] <= x_end:
                i += 1
        
        return num 
            
  # O(nlogn) as detemrined by sorting
