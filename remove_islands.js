function removeIslands(matrix) {
  let row = matrix.length;
  let col = matrix[0].length;

  function dfs(i, j) {
    if (i < 0 || j < 0 || i >= row || j >= col || matrix[i][j] !== 1) {
      return;
    }
    matrix[i][j] = 2;
    dfs(i - 1, j);
    dfs(i + 1, j);
    dfs(i, j - 1);
    dfs(i, j + 1);
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (i === 0 || i === row - 1 || j === 0 || j === col - 1) {
        dfs(i, j);
      }
    }
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (matrix[i][j] === 1) {
        matrix[i][j] = 0;
      } else if (matrix[i][j] === 2) {
        matrix[i][j] = 1;
      }
    }
  }

  return matrix;
}
