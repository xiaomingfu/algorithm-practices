// O(n) time | O(d) space
function productSum(array, level = 1) {
  // Write your code here.
  let sum = 0;
  for (let n of array) {
    if (Array.isArray(n)) {
      let subSum = productSum(n, level + 1);
      sum += subSum;
    } else {
      sum += n;
    }
  }
  return (sum *= level);
}
