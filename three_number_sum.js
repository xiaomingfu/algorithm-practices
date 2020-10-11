// O(n^2) time | O(n) space
function threeNumberSum(array, targetSum) {
  // Write your code here.
  array.sort((a, b) => a - b);
  let res = [];

  for (let i = 0; i < array.length; i++) {
    let j = i + 1;
    let k = array.length - 1;
    while (j < k) {
      const tempSum = array[i] + array[j] + array[k];
      if (tempSum === targetSum) {
        res.push([array[i], array[j], array[k]]);
        j++;
        k--;
      } else if (tempSum > targetSum) {
        k--;
      } else {
        j++;
      }
    }
  }
  return res;
}
