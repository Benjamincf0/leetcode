# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time: O(n) ; n = # nodes
        # Space: O(h) ; h = height of tree h = n in worst case => O(n) space
        self.numGoodNodes = 0;

        def dfs(root, maxVal):
            if not root: return None

            if root.val >= maxVal:
                # We have a good node on our hands.
                self.numGoodNodes += 1

            newMaxVal = max(maxVal, root.val)

            dfs(root.left, newMaxVal)
            dfs(root.right, newMaxVal)

        dfs(root, -101)

        return self.numGoodNodes