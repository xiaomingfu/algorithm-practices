class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
// O(n) time, O(n) space
function branchSums(root) {
  const sums = [];

  function dfs(node, ps) {
    if (!node) {
      return;
    }
    const newPathSum = node.value + ps;
    if (!node.left && !node.right) {
      sums.push(newPathSum);
    }
    dfs(node.left, newPathSum);
    dfs(node.right, newPathSum);
  }

  dfs(root, 0);
  return sums;
}
