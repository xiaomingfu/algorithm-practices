function caesarCipherEncryptor(string, key) {
  // Write your code here.
  let i = 0;
  let res = "";
  while (i < string.length) {
    const code = string.charCodeAt(i);
    const zCode = "z".charCodeAt(0);
    const aCode = "a".charCodeAt(0);
    const newKey = key % 26;
    if (code + newKey > zCode) {
      res = res + String.fromCharCode(((code + newKey) % zCode) - 1 + aCode);
    } else {
      res = res + String.fromCharCode(code + newKey);
    }
    i++;
  }
  return res;
}
