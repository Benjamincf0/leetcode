# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        def dfs(node):
            if node is None: return

            l = dfs(node.left)
            if l is not None: return l
            self.n+=1
            if self.n == k: return node.val
            r = dfs(node.right)
            if r is not None: return r

        return dfs(root)