function generateDocument(characters, document) {
  const dic = {};
  for (let c of characters) {
    dic[c] = (dic[c] || 0) + 1;
  }
  for (let c of document) {
    if (!dic[c] || dic[c] === 0) {
      return false;
    } else {
      dic[c]--;
    }
  }
  return true;
}
