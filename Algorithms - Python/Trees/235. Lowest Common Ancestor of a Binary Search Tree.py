# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Current node values
        curr_val = root.val
        p_val = p.val
        q_val = q.val
    
        # All on the right side
        if p_val > curr_val and q_val > curr_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # All on the left side
        elif p_val < curr_val and q_val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Find the LCA node
        else:
            return root
        
