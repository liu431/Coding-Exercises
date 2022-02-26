# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list
        res = []
        
        # Recusive function
        def addValues(root):
            if root:
                # Step 1 − Recursively traverse left subtree.
                addValues(root.left)
                # Step 2 − Recursively traverse right subtree.
                addValues(root.right)
                # Step 3 − Visit root node.
                res.append(root.val)
            
        addValues(root)
        
        return res
        
