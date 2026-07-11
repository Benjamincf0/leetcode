class LRUCache:
    class Node:
        def __init__(self, key, val):
            self._key = key
            self.val = val
            self.left = None
            self.right = None
    def __init__(self, capacity: int):
        self.hm = dict()
        self.root = None
        self.size = 0
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if self.size == 0: return -1

        # Move to the end of the cache.
        node = self.hm.get(key, None)
        if node is None: return -1 

        if node == self.root:
            return node.val

        # # detach node from ll
        node.left.right = node.right
        node.right.left = node.left

        # reattach to front
        node.left = self.root.left
        node.right = self.root

        self.root.left.right = node
        self.root.left = node
        self.root = node
        return node.val
        
    def _delete(self, node: Node) -> None:
        self.hm.pop(node._key)
        if self.size == 1: 
            self.root = None
            self.size = 0
            return
        
        if self.root == node:
            self.root = node.right
        node.left.right = node.right
        node.right.left = node.left
        self.size-=1
        

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)

        if key in self.hm:
            # remove existing node
            existingNode = self.hm[key]
            self._delete(existingNode)
        elif self.size == self.capacity:
            # delete last node
            lastNode = self.root.left
            self._delete(lastNode)

        if self.size == 0:
            self.hm[key] = node
            self.root = node
            node.left = node
            node.right = node
            self.size += 1
            return None
        
        self.hm[key] = node
        node.right = self.root
        node.left = self.root.left
        node.right.left = node
        node.left.right = node
        self.root = node
        self.size += 1