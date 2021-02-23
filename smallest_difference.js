// O(nlog(n) + mlog(m)) time | O(1) space
function smallestDifference(arrayOne, arrayTwo) {
  // Write your code here.
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  let res = [arrayOne[0], arrayTwo[0]];

  let i = 0;
  let j = 0;
  while (i < arrayOne.length && j < arrayTwo.length) {
    if (Math.abs(arrayOne[i] - arrayTwo[j]) < Math.abs(res[0] - res[1])) {
      res = [arrayOne[i], arrayTwo[j]];
    }
    if (arrayOne[i] < arrayTwo[j]) {
      i++;
    } else if (arrayOne[i] > arrayTwo[j]) {
      j++;
    } else {
      return [arrayOne[i], arrayTwo[j]];
    }
  }
  return res;
}
