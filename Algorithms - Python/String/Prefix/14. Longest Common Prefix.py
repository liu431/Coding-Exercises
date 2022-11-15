# Method 1: use set
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = min([len(s) for s in strs])
        res = ''
        for i in range(lens):
            letter = [s[i] for s in strs]
            letter_set = set(letter)
            if len(letter_set) == 1:
                res += letter[0]
            else:
                break
        return res
            
        
 # Method 2: use string index
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            shortest = min(strs, key=len)
            for i, char in enumerate(shortest):
                for other in strs:
                    if other[i] != char:
                        return shortest[:i]
            return shortest

        
