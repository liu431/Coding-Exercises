class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings will result in two identical strings if t is an anagram of s
        return sorted(s) == sorted(t)
        
