class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting
        #return sorted(s) == sorted(t)
        # Hash map
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        return dic_s == dic_t
        
