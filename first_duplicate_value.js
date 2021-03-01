// O(n^2) time | O(1) space
function firstDuplicateValue(array) {
  let smIdx = Infinity;
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] === array[j]) {
        smIdx = Math.min(j, smIdx);
      }
    }
  }
  if (smIdx !== Infinity) {
    return array[smIdx];
  }
  return -1;
}

// O(n) time | O(n) space
function firstDuplicateValue(array) {
  let dic = {};
  for (const value of array) {
    if (dic[value]) {
      return value;
    }
    dic[value] = true;
  }
  return -1;
}
// third solution
function firstDuplicateValue(array) {
  let seen = new Set();
  for (const value of array) {
    if (seen.has(value)) {
      return value;
    }
    seen.add(value);
  }
  return -1;
}
