class LinkedList {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function mergeLinkedLists(headOne, headTwo) {
  const dummyHead = new LinkedList(0);
  let node = dummyHead;
  while (headOne || headTwo) {
    if (!headOne || (headTwo && headTwo.val <= headOne.val)) {
      node.next = headTwo;
      headTwo = headTwo.next;
    } else {
      node.next = headOne;
      headOne = headOne.next;
    }
    node = node.next;
  }
  return dummyHead.next;
}
