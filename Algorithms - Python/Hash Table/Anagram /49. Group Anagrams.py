class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            i_sorted = ''.join(sorted(i))
            if i_sorted not in dic:
                dic[i_sorted] = [i]
            else:
                dic[i_sorted].append(i)
        res = []
        for key in dic:
            res.append(dic[key])

        return res
