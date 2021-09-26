function quickSort(array) {
  function qs(i, j) {
    if (i >= j) {
      return;
    }
    let l = i;
    let p = j;
    let r = j - 1;
    while (l <= r) {
      if (array[l] < array[p]) {
        l++;
      } else if (array[r] >= array[p]) {
        r--;
      } else {
        let temp = array[l];
        array[l] = array[r];
        array[r] = temp;
      }
    }
    let temp = array[l];
    array[l] = array[p];
    array[p] = temp;
    qs(i, r);
    qs(l + 1, j);
  }
  qs(0, array.length - 1);
  return array;
}
