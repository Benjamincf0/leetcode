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
            heightLeft, heightRight = dfs(root.left), dfs(root.right)
            self.max_diameter = max(self.max_diameter, heightLeft + heightRight)
            return max(heightLeft, heightRight) + 1
            
        dfs(root)
        return self.max_diameter