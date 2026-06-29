# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(root):
            if root is None: return 0
            rightDepth = dfs(root.right)
            leftDepth = dfs(root.left)
            
            self.max_diameter = max(self.max_diameter, rightDepth + leftDepth)
            return max(rightDepth, leftDepth)+1

        dfs(root)
        return self.max_diameter