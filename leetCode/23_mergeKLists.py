from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        def merge(a, b):
            dm = ListNode()
            cur = dm
            while a or b:
                if not b or (a and a.val <= b.val):
                    cur.next = a
                    a = a.next
                elif not a or (b and b.val < a.val):
                    cur.next = b
                    b = b.next
                cur = cur.next
            return dm.next
        
        q = deque(lists)
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            q.append(merge(a, b))
        return q[0]