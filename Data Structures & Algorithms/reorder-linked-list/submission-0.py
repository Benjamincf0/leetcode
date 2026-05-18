# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Time O(n) Space O(1)
        # First find halfway point -> slow & fast method
        # Second, reverse direction in second half
        # Thirdly, create final ordering with 2 ptrs

        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        slow_ptr_next = slow_ptr.next
        slow_ptr_next_next = slow_ptr_next.next
        slow_ptr.next = None
        while slow_ptr_next_next:
            slow_ptr_next.next = slow_ptr
            slow_ptr = slow_ptr_next
            slow_ptr_next = slow_ptr_next_next
            slow_ptr_next_next = slow_ptr_next_next.next

        l = head
        ln = head.next
        r = slow_ptr_next
        rn = slow_ptr

        while ln and rn:
            l.next = r
            r.next = ln

            l = ln
            r = rn
            ln = ln.next
            rn = rn.next