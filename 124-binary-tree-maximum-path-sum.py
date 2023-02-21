from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-1001]
        self.max_path_sum_util(root, ans)
        return ans[0]

    def max_path_sum_util(self, root, ans):
        if not root:
            return 0

        left_sum = self.max_path_sum_util(root.left, ans)
        right_sum = self.max_path_sum_util(root.right, ans)
        ans[0] = max(
            ans[0],
            root.val,
            root.val + left_sum,
            root.val + right_sum,
            root.val + left_sum + right_sum,
        )
        return max(root.val, root.val + left_sum, root.val + right_sum)
