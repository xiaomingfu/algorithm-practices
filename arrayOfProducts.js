function arrayOfProducts(array) {
  // Write your code here.
  // O(n) time, O(n) space
  let res = [];
  let cnt = 1;
  for (let i = 0; i < array.length; i++) {
    let l = i;
    let r = i;
    while (l - 1 >= 0) {
      cnt *= array[l - 1];
      l--;
    }
    while (r + 1 < array.length) {
      cnt *= array[r + 1];
      r++;
    }
    res.push(cnt);
    cnt = 1;
  }
  return res;
}
