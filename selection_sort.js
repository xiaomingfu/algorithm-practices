// O(n^2) time | O(1) space
function selectionSort(array) {
  // Write your code here.
  for (let i = 0; i < array.length - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < array[minIdx]) {
        minIdx = j;
      }
    }
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}
