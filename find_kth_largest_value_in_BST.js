function finkKthLargestValueBst(tree, k) {
  let arr = [];

  function dfs(tree) {
    if (tree === null) {
      return;
    }
    dfs(tree.right);
    if (arr.length < k) {
      arr.push(tree.value);
      dfs(tree.left);
    }
  }
  dfs(tree);
  return arr[k - 1];
}
