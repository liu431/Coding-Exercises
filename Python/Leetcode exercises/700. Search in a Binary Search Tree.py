# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Evaluate the value
        if root == None or root.val == val:
            return root
        # Recursion
        ## Go to right side
        if root.val < val:
            return self.searchBST(root.right, val)
        ## Go to left side
        else:
            return self.searchBST(root.left, val)
            
        
