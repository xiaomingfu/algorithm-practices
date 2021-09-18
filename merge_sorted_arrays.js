function mergeSortedArrays(arrays) {
  let res = [];
  function merge(a, b) {
    const arr = [];
    let i = 0;
    let j = 0;
    while (i < a.length || j < b.length) {
      if ((i < a.length && j < b.length && a[i] < b[j]) || j === b.length) {
        arr.push(a[i]);
        i++;
      } else {
        arr.push(b[j]);
        j++;
      }
    }
    return arr;
  }

  for (let arr of arrays) {
    res = merge(res, arr);
  }
  return res;
}
