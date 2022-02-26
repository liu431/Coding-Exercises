# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list
        res = []
        
        # Recusive function
        def addValues(root):
            if root:
                # Step 1 − Visit root node.
                res.append(root.val)
                # Step 2 − Recursively traverse left subtree.
                addValues(root.left)
                # Step 3 − Recursively traverse right subtree.
                addValues(root.right)
            
        addValues(root)
        
        return res
        
