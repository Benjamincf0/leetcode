# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        out = []

        while q:
            rightMostNodeVal = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightMostNodeVal = node.val
                    q.append(node.left)
                    q.append(node.right)

            if rightMostNodeVal is not None:
                out.append(rightMostNodeVal)
        
        return out