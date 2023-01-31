class Solution:
    def maxDepth(self, s: str) -> int:
        # loop through the s
        # use a stack to keep track parentheses
        # update maxD once parentheses is balanced
        maxD = 0
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                if s[i-1] == '(':
                    maxD = max(maxD, len(stack))
                stack.pop()
            else:
                maxD = max(maxD, len(stack))
        return maxD


