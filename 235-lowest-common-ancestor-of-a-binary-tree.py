# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root in [p, q]:
            return root

        la = self.lowestCommonAncestor(root.left, p, q)
        ra = self.lowestCommonAncestor(root.right, p, q)

        if la and ra:
            return root

        return la or ra
