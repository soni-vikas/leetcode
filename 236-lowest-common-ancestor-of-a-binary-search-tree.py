# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            p, q = q, p

        return self.lca_util(root, p, q)

    def lca_util(self, root, p, q):
        if p.val <= root.val <= q.val:
            return root

        if q.val <= root.val:
            return self.lca_util(root.left, p, q)

        else:
            return self.lca_util(root.right, p, q)
