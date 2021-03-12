function numberOfWaysToMakeChange(n, denoms) {
  let res = new Array(n + 1).fill(0);
  res[0] = 1;
  for (let d of denoms) {
    for (let i = 1; i <= n; i++) {
      if (d <= i) {
        res[i] += res[i - d];
      }
    }
  }
  return res[n];
}
