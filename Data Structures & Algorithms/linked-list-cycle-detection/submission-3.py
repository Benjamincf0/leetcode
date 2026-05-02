# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time O(n) Space O(1)
        if not head or not head.next: return False
        slow_ptr = head
        fast_ptr = head.next

        while slow_ptr and fast_ptr and fast_ptr.next:
            if slow_ptr == fast_ptr: return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return False