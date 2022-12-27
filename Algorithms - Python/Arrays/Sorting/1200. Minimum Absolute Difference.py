class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffs = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        diff_min = min(diffs)
        res = []
        for index, diff in enumerate(diffs):
            if diff == diff_min:
                res.append([arr[index], arr[index + 1]])
        print(res)
        return res


# Complexity: O(NlogN) for sorting + O(N) for getting differences + O(N) for getting min + O(N) for filtering results -> O(NlogN)
