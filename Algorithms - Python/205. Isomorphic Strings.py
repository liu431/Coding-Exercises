class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charmap = {} # Map to store the character relationships
        seen = set() # Set to track characters in t
        
        for i in range(len(s)):
            # New pair
            if s[i] not in charmap and t[i] not in seen:
                charmap[s[i]] = t[i]
                seen.add(t[i])
            # New char in s but char in t has been seen
            elif s[i] not in charmap and t[i] in seen:
                return False
            # Repetitive char in s but char in t is the one that s has been mapped to
            elif charmap[s[i]] != t[i]:
                return False
        return True
            
        
