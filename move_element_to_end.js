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
