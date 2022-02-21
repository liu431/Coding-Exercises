class Solution:
    def isValid(self, s: str) -> bool:    
        # Return False if there are odd number of characters
        if len(s) % 2 == 1:
            return False
        
        # Loop through all characters to valid parentheses
        bracket_pair = {"(": ")", "[": "]",  "{": "}"}
        stack = []
        for i in s:
            # Opening bracket
            if i in ["(", "[", "{"]:
                stack.append(i)
            # Closing bracket -> cancel off if it matches with the latest opening bracket
            elif stack and i == bracket_pair[stack[-1]]:
                stack.pop()
            else:
                return False
            
        return stack == []
            
            
            
            
        
