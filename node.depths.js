function nodeDepths(root) {
  // Write your code here.
  // O(n) time | O(n) space
  if (!root) {
    return 0;
  }
  let res = 0;
  let level = [root];
  let depth = 0;
  while (level.lengh > 0) {
    let newLevel = [];
    for (let node of level) {
      res += depth;
      if (node.left) {
        newLevel.push(node.left);
      }
      if (node.right) {
        newLevel.push(node.right);
      }
    }
    level = newLevel;
    depth++;
  }
  return res;
}

// second solution
function nodeDepths(root) {
  // when the tree is balanced, O(n) time | O(h) space
  let sumOfDepths = 0;

  function dfs(node, depth) {
    if (node) {
      sumOfDepths += depth;
      dfs(node.left, depth + 1);
      dfs(node.right, depth + 1);
    }
  }
  dfs(root, 0);
  return sumOfDepths;
}
