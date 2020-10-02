function nodeDepths(root) {
  // Write your code here.
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
