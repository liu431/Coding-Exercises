# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

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
                
        return [sum(i)/len(i) for i in levels]
            
        
