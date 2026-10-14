# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        first = res

        while head:
            prev = head
            cur = prev.next
            nxt = cur.next if cur else None

            i = cur
            for _ in range(k-1):
                if not i:
                    first.next = head
                    return res.next
                i = i.next

            for _ in range(k-1):
                cur.next = prev
                prev = cur
                cur = nxt
                nxt = nxt.next if nxt else None

            first.next = prev
            first = head
            head.next = None
            head = cur

        return res.next