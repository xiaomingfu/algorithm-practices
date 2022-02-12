# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # devide the list into half
        # reverse the second part
        # merge the two list
        
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        p, q = head, s.next
        s.next = None
        dm = ListNode(0)
        while q:
            node = q
            q = q.next
            node.next = dm.next
            dm.next = node
        q = dm.next
        dm = ListNode(0)
        cur = dm
        while q or p:
            if p:
                cur.next = p
                p = p.next
                cur = cur.next
            if q:
                cur.next = q
                q = q.next
                cur = cur.next
        return dm.next