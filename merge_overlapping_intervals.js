function mergeOverlappingIntervals(array) {
  array.sort((a, b) => a[0] - b[0]);
  const res = [];
  let l = Infinity;
  let r = -Infinity;
  for (let p of array) {
    const s = p[0];
    const e = p[1];
    if (s <= r) {
      l = Math.min(l, s);
      r = Math.max(r, e);
    } else {
      res.push([l, r]);
      l = s;
      r = e;
    }
  }
  res.push([l, r]);
  return res.slice(1);
}
