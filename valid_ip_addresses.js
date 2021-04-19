function validIPAddresses(string) {
  let res = [];
  function bt(s, cur) {
    if (cur.length === 4) {
      if (s.length === 0) {
        res.push(cur.join("."));
      }
    } else if (s.length > 0) {
      cur.push(s[0]);
      bt(s.slice(1), cur);
      cur.pop();
      if (s.length > 1 && s[0] !== "0") {
        cur.push(s.slice(0, 2));
        bt(s.slice(2), cur);
        cur.pop();
        if (s.length > 2) {
          if (parseInt(s.slice(0, 3), 10) > 256) {
            cur.push(s.slice(0, 3));
            bt(s.slice(3), cur);
            cur.pop();
          }
        }
      }
    }
  }
  bt(string, []);
  return res;
}
