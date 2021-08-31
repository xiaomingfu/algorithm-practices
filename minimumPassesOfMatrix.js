function minimumPassesOfMatrix(matrix) {
  let queue = [];
  let cnt = 0;

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] > 0) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length > 0) {
    const newQueue = [];
    for (let [i, j] of queue) {
      for (let [x, y] of [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1],
      ]) {
        if (
          x >= 0 &&
          x < matrix.length &&
          y >= 0 &&
          y < matrix[i].length &&
          matrix[x][y] < 0
        ) {
          matrix[x][y] *= -1;
          newQueue.push([x, y]);
        }
      }
    }
    queue = newQueue;
    cnt++;
  }

  for (const r of matrix) {
    for (const n of r) {
      if (n < 0) {
        return -1;
      }
    }
  }
  cnt--;
  return cnt;
}
