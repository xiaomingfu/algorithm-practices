function kadaneAlgorithm(array) {
  let res = -Infinity;
  let cur = 0;
  for (let n of array) {
    cur += n;
    res = Math.max(res, cur);
    cur = Math.max(cur, 0);
  }
  return res;
}

//
function kadaneAlgorithm(array) {
  let maxByEnd = array[0];
  let maxSum = array[0];
  for (let i = 1; i < array.length; i++) {
    maxByEnd = Math.max(maxByEnd + array[i], array[i]);
    maxSum = Math.max(maxSum, maxByEnd);
  }
  return maxSum;
}
