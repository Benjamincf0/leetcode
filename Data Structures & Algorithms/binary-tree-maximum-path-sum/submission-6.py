# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(root):
            if root is None: return 0

            return root.val + max(
                dfs(root.left),
                dfs(root.right),
                0
            )

        @cache
        def maxPath(root):
            if root is None: return float("-inf")
            return max(
                root.val + dfs(root.left) + dfs(root.right),
                dfs(root),
                maxPath(root.left),
                maxPath(root.right),
                root.val
            )

        return maxPath(root)

#           -15
#       10      20
#      N  N    15  5
#            -5 -6