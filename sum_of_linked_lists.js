class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function sumOfLinkedLists(linkedListOne, linkedListTwo) {
  const dummy = new LinkedList(0);
  let cur = dummy;
  let carry = 0;
  while (linkedListOne !== null || linkedListTwo !== null || carry > 0) {
    if (linkedListOne !== null) {
      carry += linkedListOne.value;
      linkedListOne = linkedListOne.next;
    }
    if (linkedListTwo !== null) {
      carry += linkedListTwo.value;
      linkedListTwo = linkedListTwo.next;
    }
    const node = new LinkedList(carry % 10);
    cur.next = node;
    cur = cur.next;
    carry = Math.floor(carry / 10);
  }
  return dummy.next;
}
