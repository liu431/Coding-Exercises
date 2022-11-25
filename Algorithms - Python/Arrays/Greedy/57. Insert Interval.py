class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        i, n = 0, len(intervals)
        
        # add all intervals starting before newInterval
        while i < n and newInterval[0] > intervals[i][0]:
            out.append(intervals[i])
            i += 1

        # add newInterval
        ## no overlap
        if not out or out[-1][1] < newInterval[0]:
            out.append(newInterval)
        ## overlap - merge with the current last interval
        else:
            out[-1][1] = max(out[-1][1], newInterval[1])

        # add next intervals with condition
        while i < n:
            interval = intervals[i]
            i += 1
            # no overlap
            if out[-1][1] < interval[0]:
                out.append(interval)
            # overlap
            else:
                out[-1][1] = max(out[-1][1], interval[1])

        return out
