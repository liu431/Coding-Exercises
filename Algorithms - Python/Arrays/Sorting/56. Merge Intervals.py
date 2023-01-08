class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort array by the first element
        intervals = sorted(intervals, key=lambda x: x[0])
        # initialize the result using the first list
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # update the most recent result listif there is an overlap
            if intervals[i][0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0] , intervals[i][0])
                res[-1][1] = max(res[-1][1] , intervals[i][1])
            # append the result if there is no overlap
            else:
                res.append(intervals[i])
        return res
