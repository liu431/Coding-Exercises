class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # import collections
        # dic = collections.Counter(arr)
        dic = {i:arr.count(i) for i in set(arr)}
        occurrences = dic.values()
        return len(set(occurrences)) == len(occurrences)
