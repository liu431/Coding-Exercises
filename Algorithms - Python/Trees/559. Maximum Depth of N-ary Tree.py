"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # DFS, updating the max depth at each visit.
        stack = []
        if root is not None:
            # initialize the stack with root
            stack.append((1, root))
        
        depth = 0

        while stack != []:
            c_depth, root = stack.pop()
            if root is not None:
                depth = max(c_depth, depth)
                for c in root.children:
                    stack.append((c_depth + 1, c))

        return depth
