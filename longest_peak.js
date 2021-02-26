// O(n) time | O(1) space
function longestPeak(array) {
  let len = 0;
  let cnt = 0;
  for (let i = 1; i < array.length - 1; i++) {
    if (array[i] > array[i - 1] && array[i] > array[i + 1]) {
      let l = i;
      cnt = 1;
      while (array[l] > array[l - 1] && l > 0) {
        cnt++;
        l--;
      }
      let r = i;
      while (array[r] > array[r + 1] && r < array.length - 1) {
        cnt++;
        r++;
      }
    }
    len = Math.max(len, cnt);
  }
  return len;
}
