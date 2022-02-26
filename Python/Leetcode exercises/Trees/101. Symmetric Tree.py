# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    # Recursive function
    def isMirror(self, t1, t2):
        # Reach the end leaves
        if t1 is None and t2 is None:
            return True
        # One part reaches the end
        if t1 is None or t2 is None:
            return False
        # Return True after traversing the entire input tree 
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        
