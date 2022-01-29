function findClosestValueInBst(tree, target) {
  if (!tree) {
    return Infinity;
  }
  let res = tree.value;

  if (target < res) {
    let leftRes = findClosestValueInBst(tree.left, target);
    if (Math.abs(leftRes - target) < Math.abs(res - target)) {
      res = leftRes;
    }
  }

  if (target > res) {
    let rightRes = findClosestValueInBst(tree.right, target);
    if (Math.abs(rightRes - target) < Math.abs(res - target)) {
      res = rightRes;
    }
  }
  return res;
}

// second method
function findClosestValueInBst(tree, target) {
  // Write your code here.
  // average:O(log(n)) time, O(log(n)) space
  // 	worst:O(n) time, O(n) space
  let res = tree.value;
  function dfs(node) {
    if (node === null) {
      return res;
    }
    if (Math.abs(node.value - target) < Math.abs(res - target)) {
      res = node.value;
    }
    if (node.value > target) {
      return dfs(node.left);
    } else if (node.value < target) {
      return dfs(node.right);
    } else {
      return res;
    }
  }
  return dfs(tree);
}

// third method
function findClosestValueInBst(tree, target) {
  // Write your code here.
  // 	worst: O(n) time, O(1) space
  // 	average: O(log(n)) time, O(1) space
  let res = tree.value;

  while (tree) {
    if (Math.abs(tree.value - target) < Math.abs(res - target)) {
      res = tree.value;
    }
    if (tree.value < target) {
      tree = tree.right;
    } else if (tree.value > target) {
      tree = tree.left;
    } else {
      break;
    }
  }
  return res;
}

function findClosestValueInBst(tree, target) {
  let cur = tree;
  let diff = tree.value - target;
  let res = cur.value;
  while (cur) {
    if (cur.value > target) {
      cur = cur.left;
    } else if (cur.value < target) {
      cur = cur.right;
    } else {
      return cur.value;
    }
    if (diff > cur.value - target) {
      diff = cur.value - target;
      res = cur.value;
    }
  }
  return res;
}
