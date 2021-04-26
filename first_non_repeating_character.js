function firstNonRepeatingCharacter(string) {
  let dic = {};
  for (let c of string) {
    dic[c] = (dic[c] || 0) + 1;
  }
  for (let i = 0; i < string.length; i++) {
    if (dic[string[i]] === 1) {
      return i;
    }
  }
  return -1;
}
