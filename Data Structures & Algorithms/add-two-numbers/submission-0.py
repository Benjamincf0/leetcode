# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode()
        curr = s

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1+n2+curr.val
            curr.val = total%10
            carry = total//10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or carry > 0:
                curr.next = ListNode(carry)
                curr = curr.next


        return s