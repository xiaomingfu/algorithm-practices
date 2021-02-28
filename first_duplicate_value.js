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
