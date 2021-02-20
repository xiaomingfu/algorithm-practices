function classPhotos(redShirtHeights, blueShirtHeights) {
  // O(nlog(n)) time, O(1) space
  redShirtHeights.sort((a, b) => a - b);
  blueShirtHeights.sort((a, b) => a - b);
  const firstRow = redShirtHeights[0] < blueShirtHeights[0] ? "RED" : "BLUE";
  for (let i = 0; i < redShirtHeights.length; i++) {
    if (firstRow === "RED") {
      if (redShirtHeights[i] >= blueShirtHeights[i]) {
        return false;
      }
    } else {
      if (redShirtHeights[i] <= blueShirtHeights[i]) {
        return false;
      }
    }
    return true;
  }
}
