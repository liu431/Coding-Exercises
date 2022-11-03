class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {i:ind for ind, i in enumerate(arr2)}

        res_ind = []
        lens = len(arr1)+1
        for i in arr1:
            if i in arr2_map:
                res_ind.append(arr2_map[i])
            else:
                res_ind.append(lens)
        
        return [x for _, x in sorted(zip(res_ind, arr1))]
