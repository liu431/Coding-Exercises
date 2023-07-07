class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        cts = 0
        # two pointers as a sliding window
        for i in range(len(word) - 4):
            for j in range(i + 5, len(word) + 1):
                cts += (set(word[i:j]) == vowel)
        return cts
