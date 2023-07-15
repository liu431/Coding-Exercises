# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Traverse the tree and record the maximum depth during the traversal.
        if not root:
            return 0

        # Recursively check the minimum height from a node 
        if root.left and root.right:
            # If both children check min between depths
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)
            return min(left_height, right_height) + 1
        # If single child check depth of child
        elif root.right:
            return self.minDepth(root.right) + 1
        elif root.left:
            return self.minDepth(root.left) + 1
        else:
            return 1
