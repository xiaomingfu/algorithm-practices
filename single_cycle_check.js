// O(n) time, O(n) space
function hasSingleCycle(array) {
  const n = array.length;
  const visited = new Array(n).fill(false);

  let i = 0;
  while (visited[i] === false) {
    visited[i] = true;
    i += array[i];
    i = ((i % n) + n) % n;
  }
  for (let n of visited) {
    if (n === false) {
      return false;
    }
  }
  return i === 0;
}

// O(n) time, O(1) space
function hasSingleCycle(array) {
  const n = array.length;
  let numVisited = 0;
  let cur = 0;
  while (numVisited < n) {
    if (numVisited > 0 && cur === 0) {
      return false;
    }
    numVisited++;
    cur += array[cur];
    cur = ((cur % n) + n) % n;
  }
  return cur === 0;
}
