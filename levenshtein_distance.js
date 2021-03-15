// O(nm) time, O(nm) space
function levenshteinDistance(str1, str2) {
  let cache = {};
  function dp(i, j) {
    let key = [i, j].toString();
    if (key in cache) {
      return cache[key];
    } else {
      if (i === str1.length || j === str2.length) {
        cache[key] = str1.length - i + str2.length - j;
      } else if (str1[i] === str2[j]) {
        cache[key] = dp(i + 1, j + 1);
      } else {
        cache[key] = 1 + Math.min(dp(i + 1, j), dp(i, j + 1), dp(i, j));
      }
      return cache[key];
    }
  }
  return dp(0, 0);
}
