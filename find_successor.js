class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.parent = null;
  }
}
// O(n) time, O(n) space
function findSuccessor(tree, node) {
  let list = [];

  function helper(tree) {
    if (tree === null) {
      return;
    }

    helper(tree.left);
    list.push(tree);
    helper(tree.right);
  }
  helper(tree);
  let i = list.indexOf(node);
  if (i === list.length - 1) {
    return null;
  } else {
    return list[i + 1];
  }
}
