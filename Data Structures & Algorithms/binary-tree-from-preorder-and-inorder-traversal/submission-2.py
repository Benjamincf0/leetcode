# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ino_map = {val: i for i, val in enumerate(inorder)}

        def dfs(pre_l, pre_r, ino_l):
            if pre_l == pre_r: return None
            root = TreeNode(val=preorder[pre_l])
            sep = ino_map[preorder[pre_l]]-ino_l
            
            root.left = dfs(pre_l+1, pre_l + sep+1, ino_l)
            root.right = dfs(pre_l + sep + 1, pre_r, ino_l+sep+1)
            return root

        return dfs(0, len(preorder), 0)

# preorder=[1,2,3,4]
# inorder=[2,1,3,4]