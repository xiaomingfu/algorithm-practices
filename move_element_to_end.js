// O(n) time | O(1) space
function moveElementToEnd(array, toMove) {
  // Write your code here.
  let j = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === toMove) {
      continue;
    } else {
      let temp = array[i];
      array[i] = array[j];
      array[j] = temp;
      j++;
    }
  }
  return array;
}
// second solution
function moveElementToEnd(array, toMove) {
  let i = 0;
  let j = array.length - 1;
  while (i < j) {
    while (i < j && array[j] === toMove) {
      j--;
    }
    if (array[i] === toMove) {
      temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
    i++;
  }
  return array;
}
