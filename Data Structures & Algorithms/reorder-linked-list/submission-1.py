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
        
        prev = slow_ptr
        curr = prev.next
        prev.next = None
        while curr:
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt

        l = head
        ln = head.next
        r = prev
        rn = prev.next
        while ln and rn:
            l.next = r
            r.next = ln

            l = ln
            r = rn
            ln = ln.next
            rn = rn.next