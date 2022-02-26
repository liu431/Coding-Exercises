# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the result list
        levels = []
        
        # Recusive function
        def addValues(root, level):
            if root:
                # Still on the previous level
                if len(levels) == level:
                    levels.append([])
                # Append the leave value
                levels[level] += [root.val]
                
                addValues(root.left, level+1)
                addValues(root.right, level+1)

            
        addValues(root, 0)
        
        return levels
        
        
