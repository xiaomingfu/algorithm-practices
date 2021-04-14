function sunsetViews(buildings, direction) {
  let i;
  let step;
  let res = [];
  if (direction === "WEST") {
    i = 0;
    step = 1;
  } else if (direction === "EAST") {
    i = buildings.length - 1;
    step = -1;
  }
  let maxHeight = 0;
  while (i >= 0 && i < buildings.length) {
    if (buildings[i] > maxHeight) {
      res.push(i);
    }
    maxHeight = Math.max(buildings[i], maxHeight);
    i += step;
  }
  if (direction === "EAST") {
    res.sort((a, b) => a - b);
  }
  return res;
}
