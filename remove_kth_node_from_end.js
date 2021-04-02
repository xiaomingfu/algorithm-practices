class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeKthNodeFromEnd(head, k) {
  const dummyHead = new LinkedList(0);
  dummyHead.next = head;
  let s = dummyHead;
  let f = dummyHead;
  while (k >= 0) {
    f = f.next;
    k--;
  }
  if (f === null) {
    head.value = head.next.value;
    head.next = head.next.next;
    return;
  }
  while (f !== null) {
    s = s.next;
    f = f.next;
  }
  s.next = s.next.next;
}
