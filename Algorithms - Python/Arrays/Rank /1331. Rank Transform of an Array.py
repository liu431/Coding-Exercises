class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(list(set(arr)))
        dic_r = {}
        # build a dic for unqiue element and rank
        for ind, e in enumerate(arr_sort):
            dic_r[e] = ind + 1
        # assign rank
        for ind, e in enumerate(arr):
            arr[ind] = dic_r[e]

        return arr
