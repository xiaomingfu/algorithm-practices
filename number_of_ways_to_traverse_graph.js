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
