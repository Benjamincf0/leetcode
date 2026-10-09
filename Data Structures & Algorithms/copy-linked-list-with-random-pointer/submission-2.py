"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time: O(n) ; space O(n)
        if not head: return
        d = dict()

        curr = head
        while curr: # O(n)
            d[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr: # O(n)
            if curr.next: d[curr].next = d[curr.next]
            if curr.random: d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]