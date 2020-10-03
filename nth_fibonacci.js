// solution 1 O(n^2) time | O(n) space
function getNthFib(n) {
  // Write your code here.
  if (n === 1) {
    return 0;
  }
  if (n === 2) {
    return 1;
  }
  return getNthFib(n - 1) + getNthFib(n - 2);
}
// solution 2 O(n) time | O(n) space
function getNthFib(n, memoize = { 1: 0, 2: 1 }) {
  // Write your code here.
  if (n in memoize) {
    return memoize[n];
  } else {
    memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize);
    return memoize[n];
  }
}

// solution 3 O(n) time | O(1) space
function getNthFib(n) {
  // Write your code here.
  let lastTwo = [0, 1];
  let counter = 3;

  while (counter <= n) {
    const nextFib = lastTwo[0] + lastTwo[1];
    lastTwo[0] = lastTwo[1];
    lastTwo[1] = nextFib;
    counter++;
  }
  return n > 1 ? lastTwo[1] : lastTwo[0];
}
