// O(n)time | O(d) space
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function validateBst(tree) {
  function helper(tree, min, max) {
    if (tree === null) {
      return true;
    }
    if ((tree.value < min) | (tree.value >= max)) {
      return false;
    }
    return (
      helper(tree.left, min, tree.value) && helper(tree.right, tree.value, max)
    );
  }
  return helper(tree, -Infinity, Infinity);
}
