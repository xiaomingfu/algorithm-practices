function isMonotonic(array) {
  // Write your code here.
  if (array.length < 2) {
    return true;
  }
  while (i < array.length) {
    if (array[i] > array[i - 1]) {
      i++;
      if (array[i] <= array[i - 1]) {
        return false;
      }
    } else if (array[i] < array[i - 1]) {
      i++;
      if (array[i] >= array[i - 1]) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
}
