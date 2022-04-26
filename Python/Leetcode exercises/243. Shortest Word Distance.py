class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Get all indexes of word occurrences
        w1_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word1] 
        w2_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]
        
        # Find closest indexes as the shortest distance
        return min([abs(i1-i2) for i1 in w1_ind for i2 in w2_ind])

# 4/25/22: use one-pass loop   
 class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        f1, f2 = 0, 0
        for ind, word in enumerate(wordsDict):
            if word == word1:
                word1ind = ind
                f1 = 1
            if word == word2:
                word2ind = ind
                f2 = 1
            if f1 & f2:
                res = min(res, abs(word1ind-word2ind))
        return res       
