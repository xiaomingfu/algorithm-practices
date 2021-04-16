function longestPalindromicSubstring(string) {
  let res = "";
  let resLen = 0;
  for (let i = 0; i < string.length; i++) {
    for (let [p, q] of [
      [i, i],
      [i + 1, i],
    ]) {
      while (
        p - 1 >= 0 &&
        q + 1 < stirng.length &&
        string[p - 1] === string[q + 1]
      ) {
        p--;
        q++;
      }
      if (q - p + 1 > resLen) {
        res = string.slice(p, q + 1);
        resLen = q - p + 1;
      }
    }
  }
  return res;
}
