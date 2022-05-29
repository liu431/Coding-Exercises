# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Recursive function
        def traverse(root, set_vals):
            if not root:
                return False        
            if k - root.val in set_vals:
                return True
            set_vals.add(root.val)
            return traverse(root.left, set_vals) or traverse(root.right, set_vals)
        
        return traverse(root, set())
            
        
