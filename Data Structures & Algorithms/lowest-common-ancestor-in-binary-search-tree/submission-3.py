# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest_ancestor = None
        self.lowest_level = -1
        def isAncestorOfPandQ(root, level):
            if root is None: return (False, False)

            hasP = root.val == p.val
            hasQ = root.val == q.val

            if not hasP or not hasQ:
                leftHasQ, leftHasP = isAncestorOfPandQ(root.left, level+1)
                rightHasQ, rightHasP = isAncestorOfPandQ(root.right, level+1)
                hasP = leftHasP or rightHasP or root.val == p.val
                hasQ = leftHasQ or rightHasQ or root.val == q.val
                
            isAncestor = hasQ and hasP

            if isAncestor and level > self.lowest_level:
                self.lowest_ancestor = root
                self.lowest_level = level

            return (hasQ, hasP)

        isAncestorOfPandQ(root, 0)

        return self.lowest_ancestor
