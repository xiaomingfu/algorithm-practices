function longestCommonSubsequence(str1, str2) {
  const map = new Map();
  function helper(s1, s2) {
    const key = s1 + "," + s2;
    if (!map.has(key)) {
      if (s1.length === 0 || s2.length === 0) {
        map.set(key, []);
      } else if (s1[0] === s2[0]) {
        map.set(key, [s1[0]].concat(helper(s1.slice(1), s2.slice(1))));
      } else {
        const a = helper(s1.slice(1), s2);
        const b = helper(s1, s2.slice(1));
        if (a.length > b.length) {
          map.set(key, a);
        } else {
          map.set(key, b);
        }
      }
    }
    return map.get(key);
  }
  return helper(str1, str2);
}
