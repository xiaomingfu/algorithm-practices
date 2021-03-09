class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function binaryTreeDiameter(tree) {
  let maxDiameter = 0;

  function dfs(tree) {
    if (tree === null) {
      return -1;
    }
    let left_h = dfs(tree.left);
    let right_h = dfs(tree.right);
    maxDiameter = Math.max(maxDiameter, left_h + right_h + 2);
    return Math.max(left_h, right_h) + 1;
  }
  dfs(tree);
  return maxDiameter;
}
