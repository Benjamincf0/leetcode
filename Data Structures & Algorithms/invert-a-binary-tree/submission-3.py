# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        toExplore = [root]
        inOrder = []
        if root is None: return None

        while len(toExplore) > 0:
            curr = toExplore.pop()
            inOrder.append(curr)
            if curr.left:
                toExplore.append(curr.left)
            if curr.right:
                toExplore.append(curr.right)

            
        for node in reversed(inOrder):
            node.left, node.right = node.right, node.left

        return root