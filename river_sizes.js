function riverSizes(matrix) {
  function explore(i, j) {
    let cnt = 0;
    function dfs(i, j) {
      if (
        i < 0 ||
        i >= matrix.length ||
        j < 0 ||
        j >= matrix[0].length ||
        matrix[i][j] !== 1
      ) {
        return;
      }
      matrix[i][j] = 2;
      cnt++;
      dfs(i + 1, j);
      dfs(i - 1, j);
      dfs(i, j - 1);
      dfs(i, j + 1);
    }
    dfs(i, j);
    return cnt;
  }

  let res = [];
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] === 1) {
        res.push(explore(i, j));
      }
    }
  }
  return res;
}
