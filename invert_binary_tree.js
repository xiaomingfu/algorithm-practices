// O(n) time, O(log(n)) space
function invertBinaryTree(tree) {
  if (tree === null) {
    return;
  }
  let temp = tree.left;
  tree.left = tree.right;
  tree.right = temp;
  invertBinaryTree(tree.left);
  invertBinaryTree(tree.right);
}

// O(n) time, O(n) space
function invertBinaryTree(tree) {
  let queue = [tree];
  while (queue) {
    let current = queue.shift();
    if (current === null) {
      continue;
    }
    queue.push(current.left);
    queue.push(current.right);
    let temp = current.left;
    current.left = current.right;
    current.right = temp;
  }
}
