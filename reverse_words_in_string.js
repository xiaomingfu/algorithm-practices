function reverseWordsInString(string) {
  let res = [];
  let startIdx = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === " ") {
      res.push(string.slice(startIdx, i));
      startIdx = i;
    } else if (string[startIdx] === " ") {
      res.push(" ");
      startIdx = i;
    }
  }
  res.push(string.slice(startIdx));
  for (let i = 0; i < res.length; i++) {
    let temp = res[i];
    res[i] === res[j];
    res[j] = temp;
  }
  return res.join("");
}
