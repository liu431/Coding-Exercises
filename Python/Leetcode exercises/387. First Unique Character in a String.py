class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Use dic to track the number of times each character appears in the string
        chardic = collections.Counter(s)
        # Check if a character is unique or not
        for ind, char in enumerate(s):
            if chardic[char] == 1:
                return ind
        return -1
            
