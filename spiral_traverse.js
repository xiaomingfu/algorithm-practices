function spiralTraverse(array) {
  // Write your code here.
  // O(n) time, O(n) space
  let rowStart = 0;
  let rowEnd = array.length - 1;
  let colStart = 0;
  let colEnd = array[0].length - 1;
  let res = [];

  while (rowStart <= rowEnd && colStart <= colEnd) {
    for (var i = colStart; i <= colEnd; i++) {
      res.push(array[rowStart][i]);
    }
    for (var j = rowStart + 1; j <= rowEnd; j++) {
      res.push(array[j][colEnd]);
    }

    for (var i = colEnd - 1; i >= colStart; i--) {
      if (rowStart === rowEnd) {
        break;
      }
      res.push(array[rowEnd][i]);
    }

    for (var j = rowEnd - 1; j > rowStart; j--) {
      if (colStart === colEnd) {
        break;
      }
      res.push(array[j][colStart]);
    }
    colStart++;
    rowStart++;
    colEnd--;
    rowEnd--;
  }
  return res;
}
