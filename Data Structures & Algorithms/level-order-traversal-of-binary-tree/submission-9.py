# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        if root is not None: q.append(root)

        out = []

        while q:
            qLen = len(q) #size of level
            level = []

            for _ in range(qLen):
                treeNode = q.popleft()
                level.append(treeNode.val)
                if treeNode.left is not None: q.append(treeNode.left)
                if treeNode.right is not None: q.append(treeNode.right)

            out.append(level)

        return out