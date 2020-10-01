class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
  const res = [];

  function dfs(node, ps) {
    if (!node) {
      return;
    }
    const newPathSum = node.value + ps;
    if (!node.left && !node.right) {
      res.push(newPathSum);
    }
    dfs(node.left, newPathSum);
    dfs(node.right, newPathSum);
  }

  dfs(root, 0);
  return res;
}
