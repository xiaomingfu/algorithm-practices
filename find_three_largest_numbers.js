// O(n) time | O(1) space
function findThreeLargestNumbers(array) {
  // Write your code here.
  let a = -Infinity;
  let b = -Infinity;
  let c = -Infinity;
  for (let n of array) {
    if (n > a) {
      c = b;
      b = a;
      a = n;
    } else if (n > b) {
      c = b;
      b = n;
    } else if (n > c) {
      c = n;
    }
  }
  return [c, b, a];
}
