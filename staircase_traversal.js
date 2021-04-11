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
