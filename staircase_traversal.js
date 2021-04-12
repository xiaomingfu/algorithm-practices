function staircaseTraversal(height, maxSteps) {
  let cnt = 0;
  function dfs(i, remain) {
    if (i === height) {
      cnt++;
    } else {
      for (let step = 1; step <= maxSteps; step++) {
        if (step <= remain) {
          remain -= step;
          dfs(i + step, remain);
          remain += step;
        }
      }
    }
  }
  dfs(0, height);
  return cnt;
}

// second solution O(n * k) time | O(n) space
function staircaseTraversal(height, maxSteps) {
  let memoize = { 0: 1, 1: 1 };
  function helper(height) {
    if (height in memoize) {
      return memoize[height];
    }
    let res = 0;
    for (let step = 1; step <= Math.min(height, maxSteps); step++) {
      res += helper(height - step);
    }
    memoize[height] = res;
    return res;
  }
  return helper(height);
}
