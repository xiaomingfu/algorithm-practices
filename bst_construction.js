class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    // Write your code here.
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

    // Do not edit the return statement of this method.
    return this;
  }

  contains(value) {
    // Write your code here.
    if (value < this.value) {
      if (this.left === null) {
        return false;
      }
      return this.left.contains(value);
    } else if (value === this.value) {
      return true;
    } else {
      if (this.right === null) {
        return false;
      }
      return this.right.contains(value);
    }
  }

  remove(value) {
    // Write your code here.
    // Do not edit the return statement of this method.
    return this;
  }
}
