function numberOfWaysToMakeChange(width, height) {
  let cache = {};
  let key = [width, height].toString();
  if (key in cache) {
    return cache[key];
  } else {
    if (width === 1 || height === 1) {
      cache[key] = 1;
    } else {
      cache[key] = numberOfWaysToMakeChange(width - 1, height - 1);
    }
    return cache[key];
  }
}

// second solution
function numberOfWaysToMakeChange(width, height) {
  let res = [];
  for (let i = 0; i < width; i++) {
    res.push([]);
    for (let j = 0; j < height; j++) {
      res[i].push(0);
    }
  }

  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      if (i === 0 || j === 0) {
        res[i][j] = 1;
      } else {
        res[i][j] = res[i - 1][j] + res[i][j - 1];
      }
    }
  }
  return res[width - 1][height - 1];
}
