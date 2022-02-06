# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from subprocess import list2cmdline


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy_head.next
    
    #second solution
        dm = ListNode()
        cur = dm
        while list1 or list2:
          if not list1 or (list2 and list2.val <= list1.val):
            cur.next = list2
            list2 = list2.next
          else:
            cur.next = list1
            list1 = list1.next
          cur = cur.next
        return dm.next