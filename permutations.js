function getPermutations(array) {
  if (array.length === 0) {
    return array;
  }
  const res;

  function dfs(remain, path) {
    if (remain.size === 0) {
      res.push([...path]);
    }
    let children = Array.from(remain);
    for (let c of children) {
      remain.delete(c);
      path.push(c);
      dfs(remain, path);
      remain.add(path.pop());
    }
  }

  const set = new Set(array);
  dfs(set, []);
  return res;
}
