class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function shiftLinkedList(head, k) {
  let node = head;
  let l = 0;
  while (node) {
    l++;
    node = node.next;
  }
  k = k % l;
  if (k < 0) {
    k += l;
  }
  if (k === 0) {
    return head;
  }
  let slow = head;
  let fast = head;
  while (k > 0) {
    fast = fast.next;
    k--;
  }
  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }
  let newHead = slow.next;
  slow.next = null;
  fast.next = head;
  return newHead;
}
