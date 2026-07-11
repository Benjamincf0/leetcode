# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    class MyQueue:
        class Node:
            def __init__(self, val, level):
                self.val = val
                self.next = None
                self.level = level

        def __init__(self):
            self.root = None
            self.tail = None

        def put(self, val, level):
            if val is None:
                return self
            node = self.Node(val, level)
            if self.root is None:
                self.root = node
            else:
                self.tail.next = node
            self.tail = node

            return self

        def pop(self):
            if self.root is None:
                return
            node = self.root
            self.root = self.root.next
            if node == self.tail:
                self.tail = self.tail.next
            return node

        def isempty(self) -> bool:
            return self.root is None

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        myq = self.MyQueue()
        myq.put(root, 0)

        idx = 0
        level = -1
        while not myq.isempty():
            curr = myq.pop()

            new_level = curr.level+1
            if new_level > level:
                level = new_level
                out.append([curr.val.val])
            else:
                out[-1].append(curr.val.val)

            print(idx, curr.val.val, level)
            # out.append(curr.val.val)

            myq.put(curr.val.left, new_level)
            myq.put(curr.val.right, new_level)
            idx += 1

        return out