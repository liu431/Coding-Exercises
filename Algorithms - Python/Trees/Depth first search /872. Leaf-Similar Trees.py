# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []

        def get_leaves(root, leave):
            if root:
                if not root.left and not root.right:
                    leave.append(root.val)
                else:
                    get_leaves(root.left, leave)
                    get_leaves(root.right, leave)
            return leave

        print(get_leaves(root1, leaves1))
        print(get_leaves(root2, leaves2))

        return leaves1 == leaves2
        
