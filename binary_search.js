function binarySearch(array, target) {
  // Write your code here.
  // O(log(n)) time, O(1) space
  let i = 0;
  let j = array.length - 1;

  while (i <= j) {
    const mid = Math.floor((j + i) / 2);
    if (array[mid] < target) {
      i = mid + 1;
    } else if (array[mid] > target) {
      j = mid - 1;
    } else {
      return mid;
    }
  }
  return -1;
}
