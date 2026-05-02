# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time O(n) Space O(n)
        hs = set()
        current = head

        while True:
            if current == None:
                return False
            elif current.next in hs:
                return True
            
            hs.add(current)
            current = current.next