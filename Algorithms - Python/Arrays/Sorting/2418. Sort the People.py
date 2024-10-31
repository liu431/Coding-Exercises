class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = [None] * len(names)
        for i, h in enumerate(heights):
            # get how many are taller
            ind = len([i for i in heights if h < i])
            res[ind] = names[i]
        return res
