// O(nd)time, O(n) space
function minNumberOfCoinsForChange(n, denoms) {
  let res = new Array(n + 1).fill(Infinity);
  res[0] = 0;
  for (let i = 1; i <= n; i++) {
    for (let d of denoms) {
      if (d <= n) {
        res[i] = Math.min(res[i], res[i - d] + 1);
      }
    }
  }
  if (res[n] === Infinity) {
    return -1;
  }
  return res[n];
}
