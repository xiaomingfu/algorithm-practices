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
