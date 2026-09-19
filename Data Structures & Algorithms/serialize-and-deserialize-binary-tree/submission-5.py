# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None: return ''

        out = []

        def preorder(node):
            if node is None:
                out.append('N')
                return

            out.append(node.val)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        res = ','.join(map(str, out))
        print(res)
        return res

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '': return None
        arr = data.split(',')
        self.i = 0

        def dfs():
            i = self.i
            if arr[i] == 'N': return None

            node = TreeNode(int(arr[i]))

            self.i += 1
            node.left = dfs()
            self.i += 1
            node.right = dfs()

            return node

        return dfs()