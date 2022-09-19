# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      def take_k(head):
        seg = head
        l = 0
        for _ in range(k - 1):
          if head:
            head = head.next
            l += 1
        if head:
          n = head.next
          head.next = None
          return n, l + 1, seg
        else:
          return None, l, seg
        
      def revert(head):
        tail = head
        dm = ListNode(-1)
        while head:
          tmp = dm.next
          dm.next = head
          head = head.next
          dm.next.next = tmp
        tail.next = None
        return dm.next, tail
      
      dm = ListNode(-1)
      cur = dm
      while head:
        head, l, seg = take_k(head)
        if l == k:
          seg, segtail = revert(seg)
          cur.next = seg
          cur = segtail
        else:
          cur.next = seg
      return dm.next