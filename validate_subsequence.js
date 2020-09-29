function isValidSubsequence(array, sequence) {
  // Write your code here.
  let i = 0;
  let j = 0;
  while (i < array.length && j < sequence.length) {
    if (array[i] === sequence[j]) {
      j++;
    }
    i++;
  }
  return j === sequence.length;
}
