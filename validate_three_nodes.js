class BST {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function validateThreeNodes(nodeOne, nodeTwo, nodeThree) {
  function contains(a, b) {
    if (!a) {
      return false;
    }
    if (a.val === b.val) {
      return true;
    }
    if (a.val < b.val) {
      return contains(a.right, b);
    }
    if (a.val > b.val) {
      return contains(a.left, b);
    }
  }
  return (
    (contains(nodeOne, nodeTwo) && contains(nodeTwo, nodeThree)) ||
    (contains(nodeThree, nodeTwo) && contains(nodeThree, nodeOne))
  );
}
