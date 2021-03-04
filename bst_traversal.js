function preOrderTraverse(tree, array) {
  if (tree === null) {
    return;
  }
  array.push(tree.value);
  preOrderTraverse(tree.left, array);
  preOrderTraverse(tree.right, array);
  return array;
}

function inOrderTraverse(tree, array) {
  if (tree === null) {
    return;
  }
  inOrderTraverse(tree.left, array);
  array.push(tree.value);
  inOrderTraverse(tree.right, array);
  return array;
}

function postOrderTraverse(tree, array) {
  if (tree === null) {
    return;
  }
  postOrderTraverse(tree.left, array);
  postOrderTraverse(tree.right, array);
  array.push(tree.value);
  return array;
}
