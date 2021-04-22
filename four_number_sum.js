function fourNumberSum(array, targetSum) {
  const res = [];
  array.sort((a, b) => a - b);
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = i + 1; j < array.length; j++) {
      const remain = targetSum - array[j] - array[i];
      for (let k = j + 1, l = array.length - 1; k < l; ) {
        if (array[k] + array[l] < remain) {
          k++;
        } else if (array[k] + array[l] > remain) {
          l--;
        } else {
          res.push([array[i], array[j], array[k], array[l]]);
        }
      }
    }
  }
  return res;
}
