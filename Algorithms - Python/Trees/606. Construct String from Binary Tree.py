# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Depth first search

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = str(root.val)
        if root.left:
            res += f"({self.tree2str(root.left)})"
        if root.right:
            # when left branch is None
            if not root.left:
                res += "()"
            res += f"({self.tree2str(root.right)})"
        return res
            
