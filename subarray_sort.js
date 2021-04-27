function subarraySort(array) {
  const res = [-1, -1];
  const sorted = array.slice().sort((a, b) => a - b);
  for (let i = 0, j = array.length - 1; i <= j; ) {
    if (array[i] !== sorted[i]) {
      res[0] = i;
    }
    if (array[j] !== sorted[j]) {
      res[1] = j;
    }
    if (res[0] === -1) {
      i++;
    }
    if (res[1] === -1) {
      j--;
    }
    if (res[0] !== -1 && res[1] !== -1) {
      return res;
    }
  }
  return res;
}

// second solution

function subarraySort(array) {
  let minUnordered = Infinity;
  let maxUnordered = -Infinity;
  let i = 0;
  let j = array.length - 1;
  while (array[i] <= array[i + 1] && i < array.length - 1) {
    i++;
  }
  if (i === array.length - 1) {
    return [-1, -1];
  }
  while (array[j] >= array[j - 1] && j >= 1) {
    j--;
  }
  let k = i;
  while (k >= i && k <= j) {
    minUnordered = Math.min(minUnordered, array[k]);
    maxUnordered = Math.max(maxUnordered, array[k]);
    k++;
  }
  i = 0;
  j = array.length - 1;
  while (array[i] <= minUnordered) {
    i++;
  }
  while (array[j] >= maxUnordered) {
    j--;
  }
  return [i, j];
}
