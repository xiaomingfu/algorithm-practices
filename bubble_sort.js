// O(n^2) time | O(1) space
function bubbleSort(array) {
  // Write your code here.
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = 0; j < array.length - i; j++) {
      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
  return array;
}

// rewrite

function bubbleSort(array) {
  let isSorted = false;
  let cnt = 0;
  while (!isSorted) {
    isSorted = true;
    for (let i = 0; i < array.length - 1 - cnt; i++) {
      if (array[i] > array[i + 1]) {
        let temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        isSorted = false;
      }
    }
    cnt++;
  }
  return array;
}
