function runLengthEncoding(string) {
  // O(n) time, O(n) space
  let res = [];
  let cnt = 1;
  for (let i = 1; i < string.length; i++) {
    if (string[i] !== string[i - 1] || cnt === 9) {
      res.push(cnt.toString());
      res.push(string[i - 1]);
      cnt = 0;
    }
    cnt++;
  }
  res.push(cnt.toString());
  res.push(string[string.length - 1]);
  return res.join("");
}
