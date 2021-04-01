constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
}

function reconstructBst(preOrderTraversalValues) {
    if (preOrderTraversalValues.length === 0) {
		return;
	}
	let root = preOrderTraversalValues[0];
	let left_sub = [];
	let right_sub = [];
	for (let i = 1; i < preOrderTraversalValues.length; i++) {
		if (preOrderTraversalValues[i] < root) {
			left_sub.push(preOrderTraversalValues[i]);
		} else {
			right_sub.push(preOrderTraversalValues[i]);
		}
	}
	let left_subTree = reconstructBst(left_sub);
	let right_subTree = reconstructBst(right_sub);
	
	return new BST(root, left_subTree, right_subTree);
}