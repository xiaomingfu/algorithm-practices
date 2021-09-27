class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function zipLinkedList(linkedList) {
  // Write your code here.
  if (linkedList === null) {
    return linkedList;
  }
  let s = linkedList;
  let f = linkedList.next;
  while (f !== null && f.next !== null) {
    s = s.next;
    f = f.next.next;
  }
  let p = linkedList;
  let q = s.next;
  s.next = null;

  const dm = new LinkedList(0);
  while (q !== null) {
    let temp = dm.next;
    dm.next = q;
    q = q.next;
    dm.next.next = temp;
  }
  q = dm.next;

  dm.next = null;
  let cur = dm;
  while (p !== null || q !== null) {
    if (p !== null) {
      cur.next = p;
      p = p.next;
      cur = cur.next;
    }
    if (q !== null) {
      cur.next = q;
      q = q.next;
      cur = cur.next;
    }
  }
  return dm.next;
}
