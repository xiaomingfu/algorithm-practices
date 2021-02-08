// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array) {
    // Write your code here.
    // O(v + e) time, O (v) space
    function dfs(node) {
      array.push(node.name);
      for (const ch of node.children) {
        dfs(ch);
      }
    }

    dfs(this);
    return array;
  }

  // another write way
  depthFirstSearch(array) {
    array.push(this.name);
    for (const ch of this.children) {
      ch.depthFirstSearch(array);
    }
    return array;
  }
}

// Do not edit the line below.
exports.Node = Node;
