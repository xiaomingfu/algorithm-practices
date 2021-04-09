function threeNumberSort(array, order) {
  const dic = {};
  for (let n of array) {
    dic[n] = dic[n] || 0 + 1;
  }
  let i = 0;
  for (let d of order) {
    if (dic[d] > 0) {
      array[i] = d;
      dic[d]--;
      i++;
    }
  }
  return array;
}
