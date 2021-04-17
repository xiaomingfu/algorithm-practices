function groupAnagrams(words) {
  let dic = {};
  for (let w of words) {
    const sw = w.split("").sort().join("");
    if (dic[sw]) {
      dic[sw].push(w);
    } else {
      dic[sw] = [w];
    }
  }
  return Object.values(dic);
}
