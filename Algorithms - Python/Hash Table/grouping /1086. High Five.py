class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''first build a dictionary for id and score list, then print out the avg of top 5'''
        dic = {}
        for i in items:
            id = i[0]
            s = i[1]
            if id not in dic:
                dic[id] = [s]
            else:
                dic[id].append(s)

        res = []
        for k, v in dic.items():
            top5 = int(sum(sorted(v)[-5:]) / 5)
            res.append([k, top5])
        
        res = sorted(res, key=lambda i: i[0])
        return res
