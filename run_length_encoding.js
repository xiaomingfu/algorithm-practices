function runLengthEncoding(string) {
  // Write your code here.
  let res = "";
  let i = 0;
  for (let j = 1; j < string.length; ) {
    let cnt = 1;
    while (string[i] === string[j] && cnt < 9) {
      j++;
      cnt++;
    }
    res += cnt + string[i];
    i = j;
    j++;
  }
  return res;
}
