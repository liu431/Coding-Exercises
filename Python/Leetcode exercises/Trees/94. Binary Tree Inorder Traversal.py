# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize results list
        res = []
        # Recursive function
        def addValues(root):
            if root:
                # Step 1 − Recursively traverse left subtree.
                addValues(root.left)
                # Step 2 − Keep root node.
                res.append(root.val)
                # Step 3 − Recursively traverse right subtree.
                addValues(root.right)
        
        # Inorder traversal
        addValues(root)
        
        return res
    

        
