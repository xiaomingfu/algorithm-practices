// O(n*2^n) time and space
function powerset(array) {
  const res = [[]];
  for (let n of array) {
    const l = res.length;
    for (let i = 0; i < l; i++) {
      res.push(res[i].concat(n));
    }
  }
  return res;
}

// second solution
function powerset(array) {
  let res = [];
  function dfs(i, cur) {
    if (i === array.length) {
      res.push([...cur]);
    } else {
      dfs(i + 1, cur);
      cur.push(array[i]);
      dfs(i + 1, cur);
      cur.pop();
    }
  }
  dfs(0, []);
  return res;
}
