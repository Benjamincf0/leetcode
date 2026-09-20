# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time O(n*log(k)) Space O(1) where n is total num nodes & k is num lists
        def merge(i, j):
            if lists[j].val < lists[i].val:
                lists[i], lists[j] = lists[j], lists[i]

            cur = lists[i]
            next1 = cur.next
            next2 = lists[j]

            # merge cur2 into cur1               
            while next1 and next2:
                if next2.val < next1.val:
                    cur.next = next2
                    next2 = next2.next
                else:
                    cur.next = next1
                    next1 = next1.next
                cur = cur.next
                    
            if next1:
                cur.next = next1

            if next2:
                cur.next = next2

            lists[j] = None

        k = 1
        while k < len(lists):
            for i in range(0, len(lists), 2*k):
                if i+k >= len(lists)-1 or not lists[i+k]: continue
                if not lists[i]:
                    lists[i] = lists[i+k]
                    lists[i+k] = None
                    continue

                merge(i, i+k)
                
            k *= 2

        if lists and lists[-1] is not None:
            merge(0, len(lists)-1)

        return lists[0] if lists else None
            

