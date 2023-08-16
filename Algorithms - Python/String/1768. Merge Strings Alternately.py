class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Merge the strings by adding letters in alternating order, starting with word1.
        alterLen = min(len(word1), len(word2))
        res = [''] * alterLen * 2
        for ind, i in enumerate(word1[:alterLen]):
            res[ind * 2] = i
        for ind, i in enumerate(word2[:alterLen]):
            res[ind * 2 + 1] = i       

        # If a string is longer than the other, append the additional letters onto the end of the merged string.
        if word1[alterLen:]:
            res += word1[alterLen:]
        if word2[alterLen:]:
            res += word2[alterLen:]        

        return ''.join(res)
