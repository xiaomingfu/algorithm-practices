class AncestralTree {
  constructor(nam) {
    this.name = name;
    this.ancestor = null;
  }
}
// O(n) time, O(1) space
function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
  // Write your code here.

  const depthOne = getDepth(descendantOne, topAncestor);
  const depthTwo = getDepth(descendantTwo, topAncestor);
  if (depthOne < depthTwo) {
    return findCommonAncestor(
      descendantOne,
      descendantTwo,
      depthTwo - depthOne
    );
  } else {
    return findCommonAncestor(
      descendantTwo,
      descendantOne,
      depthOne - depthTwo
    );
  }
}

function getDepth(descedant, topAncestor) {
  let depth = 0;
  while (descedant !== topAncestor) {
    depth++;
    descedant = descedant.ancestor;
  }
  return depth;
}

function findCommonAncestor(higherAncestor, lowerAncestor, diff) {
  while (diff > 0) {
    lowerAncestor = lowerAncestor.ancestor;
    diff--;
  }
  while (lowerAncestor !== higherAncestor) {
    lowerAncestor = lowerAncestor.ancestor;
    higherAncestor = higherAncestor.ancestor;
  }
  return lowerAncestor;
}
