function sameBsts(arrayOne, arrayTwo) {
  function partition(array, a, b) {
    const l = [];
    const r = [];
    for (let i = a + 1; i <= b; i++) {
      if (array[i] < array[a]) {
        l.push(array[i]);
      } else {
        r.push(array[i]);
      }
    }
    let cur = a + 1;
    for (let n of l) {
      array[cur] = n;
      cur++;
    }
    for (let n of r) {
      array[cur] = n;
      cur++;
    }
    return a + l.length + 1;
  }
  function helper(a, b, c, d) {
    if (b - a !== d - c) {
      return false;
    }
    if (arrayOne[a] !== arrayTwo[c]) {
      return false;
    }
    if (b < a) {
      return true;
    }
    let e = partition(arrayOne, a, b);
    let f = partition(arrayTwo, c, d);
    return helper(a + 1, e - 1, c + 1, f - 1) && helper(e, b, f, d);
  }
  return helper(0, arrayOne.length - 1, 0, arrayTwo.length - 1);
}
