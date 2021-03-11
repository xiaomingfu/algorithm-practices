function maxSubsetSumNoAdjacent(array) {
  if (!array.length) {
    return 0;
  }
  if (array.length === 1) {
    return;
  }
  let res = array.slice();
  res[1] = Math.max(res[0], res[1]);
  for (let i = 2; i < array.length; i++) {
    res[i] = Math.max(res[i - 1], res[i] + res[i - 2]);
  }
  return res[res.length - 1];
}
