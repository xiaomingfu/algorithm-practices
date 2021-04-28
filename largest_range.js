function largestRange(array) {
  array.sort((a, b) => a - b);
  let res = [-1, 0];
  let i = 0,
    j = 0;
  while (j < array.length) {
    while (
      (j < array.length - 1 && array[j + 1] === array[j] + 1) ||
      array[j + 1] === array[j]
    ) {
      j++;
    }
    if (array[j] - array[i] > res[1] - res[0]) {
      res[0] = array[i];
      res[1] = array[j];
    }
    i = j + 1;
    j = i;
  }
  return res;
}
