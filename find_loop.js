class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
// O(n)time, O(1) space
function findLoop(head) {
  let s = head.next;
  let f = head.next.next;
  while (f !== s) {
    s = s.next;
    f = f.next.next;
  }
  s = head;
  while (s !== f) {
    s = s.next;
    f = f.next;
  }
  return s;
}

function findLoop(head) {
  const set = new Set();
  let res = head;
  while (!set.has(res)) {
    set.add(res);
    res = res.next;
  }
  return res;
}
