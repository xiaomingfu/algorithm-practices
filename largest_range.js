function largestRange(array) {
  array.sort((a, b) => a - b);
  let res = [0, -1];
  let i = 0,
    j = 0;
  while (j < array.length) {
    while (
      (j < array.length - 1 && array[j + 1] === array[j] + 1) ||
      array[j + 1] === array[j]
    ) {
      j++;
    }
    if (array[j] - array[i] > res[1] - res[0]) {
      res[0] = array[i];
      res[1] = array[j];
    }
    i = j + 1;
    j = i;
  }
  return res;
}

// second solution

function largestRange(array) {
  const dic = {};
  let res = [0, -1];
  for (let n of array) {
    dic[n] = true;
  }
  for (let n of array) {
    if (dic[n]) {
      dic[n] = false;
      let left = n - 1;
      let right = n + 1;
      while (dic[left]) {
        dic[left] = false;
        left--;
      }
      while (dic[right]) {
        dic[right] = false;
        right++;
      }
      left = left - 1;
      right = right + 1;
      if (right - left > res[1] - res[0]) {
        res = [left, right];
      }
    }
  }
  return res;
}
