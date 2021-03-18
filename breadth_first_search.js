class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  //   O(v + e) time, O(v) space
  breadthFirstSearch(array) {
    let queue = [this];
    while (queue.length > 0) {
      let cur = queue.shift();
      array.push(cur.name);
      for (let child of cur.children) {
        queue.push(child);
      }
    }
    return array;
  }
}
