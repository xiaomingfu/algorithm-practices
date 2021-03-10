class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class TreeInfo {
  constructor(height, isBalanced) {
    this.height = height;
    this.isBalanced = isBalanced;
  }
}

function heightBalancedBinaryTree(tree) {
  function dfs(tree) {
    if (tree === null) {
      return new TreeInfo(-1, true);
    }

    let left_info = dfs(tree.left);
    let right_info = dfs(tree.right);
    let height = Math.max(left_info.height, right_info.height) + 1;
    let isBalanced =
      left_info.isBalanced &&
      right_info.isBalanced &&
      Math.abs(left_info.height - right_info.height) <= 1;
    return new TreeInfo(height, isBalanced);
  }

  let tree_info = dfs(tree);
  return tree_info.isBalanced;
}
