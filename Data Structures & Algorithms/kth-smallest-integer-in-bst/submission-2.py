# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        curr = root
        i = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
        
            curr = stack.pop()
            i+=1
            if i == k: return curr.val
            curr = curr.right
        
