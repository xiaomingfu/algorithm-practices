function isValidSubsequence(array, sequence) {
  // Write your code here.
  // 	O(n) time n is the length of array, O(1) space
  let seqIdx = 0;
  let arrIdx = 0;
  while (arrIdx < array.length && seqIdx < sequence.length) {
    if (sequence[seqIdx] === array[arrIdx]) {
      seqIdx++;
    }
    arrIdx++;
  }
  return seqIdx === sequence.length;
}

// solution 2

function isValidSubsequence(array, sequence) {
  // Write your code here.
  let seqIdx = 0;
  for (let n of array) {
    if (seqIdx === sequence.length) {
      break;
    }
    if (sequence[seqIdx] === n) {
      seqIdx++;
    }
  }
  return sequence.length === seqIdx;
}
