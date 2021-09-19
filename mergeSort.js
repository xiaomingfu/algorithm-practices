function mergeSort(array) {
  if (array.length <= 1) {
    return array;
  }
  const mid = Math.floor(array.length / 2);
  const left = mergeSort(array.slice(0, mid));
  const right = mergeSort(array.slice(mid));
  return merge(left, right);
}

function merge(a, b) {
  let i = 0;
  let j = 0;
  let res = [];
  while (i < a.length || j < b.length) {
    if ((i < a.length && j < b.length && a[i] < b[j]) || j === b.length) {
      res.push(a[i]);
      i++;
    } else {
      res.push(b[j]);
      j++;
    }
  }
  return res;
}
