class LinkedList {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  const dummyHead = new LinkedList(0);
  while (head) {
    const originNext = dummyHead.next;
    dummyHead.next = head;
    head = head.next;
    dummyHead.next.next = originNext;
  }
  return dummyHead.next;
}
