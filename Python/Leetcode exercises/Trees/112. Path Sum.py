# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # End of root with no path found
        if not root:
            return False
        
        # Find the path
        if not root.left and not root.right and root.val == targetSum:
            return True 

        # Increment the sum
        targetSum -= root.val
        
        # Recursion
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
            
        
