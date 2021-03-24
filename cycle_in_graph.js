function cycleInGraph(edges) {
  let int_dic = {};
  for (let v = 0; v < edges.length; v++) {
    for (let e of edges[v]) {
      int_dic[e] = (in_dic[e] || 0) + 1;
    }
  }

  let arr = [];
  for (let v = 0; v < edges.length; v++) {
    int_dic[v] = in_dic[v] || 0;
    if (int_dic[v] === 0) {
      arr.push(v);
    }
  }
  let remove = [];
  while (arr.length > 0) {
    let v = arr.shift();
    remove.push(v);
    for (let e of edges[v]) {
      int_dic[e]--;
      if (int_dic[e] === 0) {
        arr.push(e);
      }
    }
  }
  return remove.length < edges.length;
}
