# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time O(n*log(k)) Space O(1) where n is total num nodes & k is num lists
        if not lists: return None

        n = len(lists)
        step = 1
        while step < n:
            for i in range(0, n-step, 2*step):
                    lists[i] = self.merge(lists[i], lists[i+step])
                    lists[i+step]
            step *= 2

        return lists[0]

    def merge(self, l1, l2):
        root = ListNode()
        tail = root

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return root.next