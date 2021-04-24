function sortedSquaredArray(array) {
  const res = [];
  for (let i = 0, j = array.length - 1; i <= j; ) {
    if (Math.abs(array[i]) < Math.abs(array[j])) {
      res.unshift(array[j] * array[j]);
      j--;
    } else {
      res.unshift(array[i] * array[i]);
      i++;
    }
  }
  return res;
}
