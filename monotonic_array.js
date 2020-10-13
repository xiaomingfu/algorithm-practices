function isMonotonic(array) {
  // Write your code here.
  if (array.length < 2) {
    return true;
  }
  let i = 1;
  while (i < array.length) {
    if (array[i] > array[i - 1]) {
      i++;
      if (array[i] < array[i - 1]) {
        return false;
      }
    } else if (array[i] < array[i - 1]) {
      i++;
      if (array[i] > array[i - 1]) {
        return false;
      }
    } else {
      i++;
    }
  }
  return true;
}

// O(n) time | O(1) space
function isMonotonic(array) {
  // Write your code here.
  let isIncreasing = true;
  let isDecreasing = true;

  for (let i = 1; i < array.length; i++) {
    if (array[i] > array[i - 1]) {
      isDecreasing = false;
    } else if (array[i] < array[i - 1]) {
      isIncreasing = false;
    }
  }
  return isIncreasing || isDecreasing;
}
