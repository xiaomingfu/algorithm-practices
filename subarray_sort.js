function subarraySort(array) {
  const res = [-1, -1];
  const sorted = array.slice().sort((a, b) => a - b);
  for (let i = 0, j = array.length - 1; i <= j; ) {
    if (array[i] !== sorted[i]) {
      res[0] = i;
    }
    if (array[j] !== sorted[j]) {
      res[1] = j;
    }
    if (res[0] === -1) {
      i++;
    }
    if (res[1] === -1) {
      j--;
    }
    if (res[0] !== -1 && res[1] !== -1) {
      return res;
    }
  }
  return res;
}
