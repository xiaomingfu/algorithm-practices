function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
  // Write your code here.
  redShirtSpeeds.sort((a, b) => a - b);
  blueShirtSpeeds.sort((a, b) => a - b);
  const len = redShirtSpeeds.length;
  let i = 0;
  let res = 0;
  while (i < redShirtSpeeds.length) {
    if (fastest) {
      res += Math.max(redShirtSpeeds[i], blueShirtSpeeds[len - 1 - i]);
      i++;
    } else {
      res += Math.max(redShirtSpeeds[i], blueShirtSpeeds[i]);
      i++;
    }
  }
  return res;
}
