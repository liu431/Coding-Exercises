class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # wall matadata
        n_rows = len(wall)
        n_len = sum(wall[0])
        # dic for the gap counts
        gap_cts = {}
        for w in wall:
            cum_sum = 0
            for i in w[:-1]:
                cum_sum += i
                if cum_sum in gap_cts:
                    gap_cts[cum_sum] += 1
                else:
                    gap_cts[cum_sum] = 1
                    
        # get max number of gaps 
        if gap_cts:
            max_crosses = max(gap_cts.values())
        else:
            max_crosses = 0

        # return the minimum number of crossed bricks after drawing such a vertical line
        return n_rows - max_crosses
