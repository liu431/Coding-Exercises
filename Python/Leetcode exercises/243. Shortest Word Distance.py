class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Get all index occurences
        w1_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word1] 
        w2_ind = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]
        
        # Find closest indexes as the shortest distance
        return min([abs(i1-i2) for i1 in w1_ind for i2 in w2_ind])

        
        
