function minimumCharactersForWords(words) {
  const res = [];
  const dic = {};
  for (const w of words) {
    const wDic = {};
    for (const c of w) {
      wDic[c] = wDic[c] + 1 || 1;
    }
    for (c in wDic) {
      dic[c] = Math.max(dic[c], wDic[c]) || wDic[c];
    }
  }
  for (const c in dic) {
    while (dic[c]) {
      res.push(c);
      dic[c]--;
    }
  }
  return res;
}
