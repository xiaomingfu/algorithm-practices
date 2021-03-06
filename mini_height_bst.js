// O(nlog(n)) time | O(n) space
function miniHeightBst(array) {
  function helper(array, bst, i, j) {
    if (i > j) {
      return;
    }
    let mid = Math.floor((i + j) / 2);
    if (bst === null) {
      bst = new BST(array[mid]);
    } else {
      bst.insert(array[mid]);
    }
    helper(array, bst, i, mid);
    helper(array, bst, mid, j);
    return bst;
  }
  return helper(array, null, 0, array.length - 1);
}

class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (this.right === null) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }
  }
}
