// O(n^2) time | O(1) space
function insertionSort(array) {
  // Write your code here.
  for (let i = 1; i < array.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (array[j + 1] < array[j]) {
        const temp = array[j + 1];
        array[j + 1] = array[j];
        array[j] = temp;
      } else {
        break;
      }
    }
  }
  return array;
}
