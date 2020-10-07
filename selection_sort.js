// O(n^2) time | O(1) space
function selectionSort(array) {
  // Write your code here.
  let k = 0;
  for (let i = 0; i < array.length - 1; i++) {
    let min = array[i];
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < min) {
        min = array[j];
        k = j;
      }
    }
    if (min !== array[i]) {
      const temp = array[i];
      array[i] = min;
      array[k] = temp;
    }
  }
  return array;
}
