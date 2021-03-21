class AncestralTree {
  constructor(nam) {
    this.name = name;
    this.ancestor = null;
  }
}
// O(n) time, O(1) space
function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
  // Write your code here.
  let cnt_1 = 0;
  let cnt_2 = 0;
  let one = descendantOne;
  let two = descendantTwo;
  while (one !== topAncestor) {
    cnt_1++;
    one = one.ancestor;
  }
  while (two !== topAncestor) {
    cnt_2++;
    two = two.ancestor;
  }
  while (cnt_1 < cnt_2) {
    descendantTwo = descendantTwo.ancestor;
    cnt_2--;
  }
  while (cnt_1 > cnt_2) {
    descendantOne = descendantOne.ancestor;
    cnt_1--;
  }
  while (descendantOne !== descendantTwo) {
    descendantOne = descendantOne.ancestor;
    descendantTwo = descendantTwo.ancestor;
  }
  return descendantTwo;
}
