# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, p, q):
        if p is None and q is None: return True
        elif p is None or q is None: return False
        elif p.val != q.val: return False

        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None: return True
        if subRoot is None and root: return True
        if subRoot  and root is None: return False
        if self.isSametree(root,subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
