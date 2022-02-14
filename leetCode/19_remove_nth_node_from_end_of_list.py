# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dm = ListNode()
        dm.next = head
        s = dm
        f = head
        while n > 0:
            f = f.next
            n -= 1
            
        while f:
            s = s.next
            f = f.next
        s.next =s.next.next
        return dm.next