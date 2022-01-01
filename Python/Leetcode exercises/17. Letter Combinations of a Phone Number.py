class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty for empty inputs
        if len(digits) == 0:
            return []
        
        # Map all the digits to their corresponding letters
        mapp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        # Initialize the letter sets
        res = mapp[digits[0]]
        # Iterate through the digit indexs
        for ch in digits[1:]:
            res = [v + c for c in mapp[ch] for v in res]
        return res
            
            
        
