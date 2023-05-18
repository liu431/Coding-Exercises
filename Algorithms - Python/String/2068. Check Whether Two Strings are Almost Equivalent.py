class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # all letters
        word1letters = set(word1)
        word2letters = set(word2)
        letters = word1letters.union(word2letters)
        word1cts = {w: word1.count(w) for w in word1letters}
        word2cts = {w: word2.count(w) for w in word2letters}
        print(word1cts, word2cts)
        for l in letters:
            if l not in word1cts:
                word1cts[l] = 0
            if l not in word2cts:
                word2cts[l] = 0          
            if abs(word1cts[l] - word2cts[l]) > 3:
                return False
        return True
