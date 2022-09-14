class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic = {}
        for log in logs:
            birth, death = log[0], log[1]
            for i in range(birth, death):
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
        return sorted(dic.items(), key=lambda item: (-item[1], item[0]))[0][0]
            
