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

function explore2(i, j) {
  let cnt = 1;
  const queue = [[i, j]];
  matrix[i][j] = 2;
  while (queue.length > 0) {
    const [x, y] = queue.shift();
    for ([a, b] of [
      [x + 1, y],
      [x - 1, y],
      [x, y - 1],
      [x, y + 1],
    ]) {
      if (
        a >= 0 &&
        a < matrix.length &&
        b >= 0 &&
        b < matrix[0].length &&
        matrix[a][b] === 1
      ) {
        cnt++;
        matrix[a][b] = 2;
        queue.push([a, b]);
      }
    }
  }
  return cnt;
}
