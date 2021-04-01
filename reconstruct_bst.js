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
	let leftSub = [];
	let rightSub = [];
	for (let i = 1; i < preOrderTraversalValues.length; i++) {
		if (preOrderTraversalValues[i] < root) {
			leftSub.push(preOrderTraversalValues[i]);
		} else {
			rightSub.push(preOrderTraversalValues[i]);
		}
	}
	let leftSubTree = reconstructBst(leftSub);
	let rightSubTree = reconstructBst(rightSub);
	
	return new BST(root, leftSubTree, rightSubTree);
}

// second solution

function reconstructBst(preOrderTraversalValues) {
    let i = 0;
    function helper(lb, hb) {
        const value = preOrderTraversalValues[i];
        if (i === preOrderTraversalValues.length) {
            return;
        }
        if (value < lb || value >= hb) {
            return;
        }
        i++;
        const left = helper(lb, value);
        const right = helper(value, hb);
        return new BST(value, left, right);
    }
    return helper(-Infinity, Infinity);
}