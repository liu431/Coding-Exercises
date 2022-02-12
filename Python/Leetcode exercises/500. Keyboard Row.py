class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Create letter-row directory
        rows = {}
        for i, characters in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            for char in characters:
                rows[char] = i
        
        # Test each word by weather the row numbers for each letter are the same
        ## Find the row number from the letter-row dict
        ## Use set to check whether all row numbers are the same
        res = []
        for word in words:
            rownum = set([rows[i.lower()] for i in word])
            if len(rownum) == 1:
                res.append(word)
        return res
            
                
        
