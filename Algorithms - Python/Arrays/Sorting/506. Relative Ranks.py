class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankDic = {}
        scoreSorted = sorted(score, reverse = True)
        res = []
        for i in score:
            rank = scoreSorted.index(i)
            if rank == 0:
                res.append("Gold Medal")
            elif rank == 1:
                res.append("Silver Medal")
            elif rank == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(rank + 1))
        return res
