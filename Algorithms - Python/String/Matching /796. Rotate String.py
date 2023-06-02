class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False
        s, goal = [*s], [*goal]
        print(s)
        for i in range(len(s)):
            # shift the current first letter
            s = s[1:] + [s[0]]
            if s == goal:
                return True
        return False    
