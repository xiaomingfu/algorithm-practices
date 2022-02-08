# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        s = head
        f = head.next
        while s != f:
            if not f or not f.next:
                return False
            s = s.next
            f = f.next.next
        return True