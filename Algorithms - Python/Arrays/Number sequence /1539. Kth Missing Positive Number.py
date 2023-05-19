class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_all = [i for i in range(1, arr[-1] + k + 1)]
        for i in arr:
            arr_all.remove(i)
        print(arr_all)
        return arr_all[k - 1]
