class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  // Write your code here.
  let head = linkList;
  while (head && head.next) {
    if (head.value === head.next.value) {
      head.next = head.next.next;
    } else {
      head = head.next;
    }
  }
  return linkedList;
}

function removeDuplicatesFromLinkedList(node) {
  // Write your code here.
  let dummyHead = new LinkedList(node.value - 1);
  let cur = dummyHead;
  while (node) {
    if (node.value !== cur.value) {
      cur.next = node;
      cur = cur.next;
    }
    node = node.next;
  }
  cur.next = null;
  return dummyHead.next;
}
