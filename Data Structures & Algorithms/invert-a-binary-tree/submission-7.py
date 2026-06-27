# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # O(h) space O(n) time
        if root is None: return None
        s = [root]

        while len(s) > 0:
            curr = s.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left: s.append(curr.left)
            if curr.right: s.append(curr.right)

        return root