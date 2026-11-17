# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Top-down O(n)

        @cache
        def dfs(root):
            if root is None: return 0

            return root.val + max(
                dfs(root.left),
                dfs(root.right),
                0
            )

        def maxPath(root):
            if root is None: return float("-inf")
            return max(
                root.val + max(dfs(root.left),0) + max(dfs(root.right),0),
                maxPath(root.left),
                maxPath(root.right),
            )

        return maxPath(root)

#           -15
#       10      20
#      N  N    15  5
#            -5 -6