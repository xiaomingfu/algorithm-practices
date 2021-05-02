function zigzagTraverse(array) {
  const row = array.length - 1;
  const col = array[0].length - 1;
  let i = 0;
  let j = 0;
  const res = [];
  let goingDown = true;
  while (i >= 0 && i <= row && j >= 0 && j <= col) {
    res.push(array[i][j]);
    if (goingDown) {
      if (j === 0 || i === row) {
        goingDown = false;
        if (i === row) {
          j++;
        } else {
          i++;
        }
      } else {
        i++;
        j--;
      }
    } else {
      if (i === 0 || j === col) {
        goingDown = true;
        if (j === col) {
          i++;
        } else {
          j++;
        }
      } else {
        i--;
        j++;
      }
    }
  }
  return res;
}
