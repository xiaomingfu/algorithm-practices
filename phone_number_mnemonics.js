function phoneNumberMnemonics(phoneNumber) {
  const dic = {
    1: "1",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: "0",
  };
  let res = [""];
  for (let n of phoneNumber) {
    let arr = [];
    for (let c of res) {
      for (let d of dic[n]) {
        arr.push(c + d);
      }
    }
    res = arr;
  }
  return res;
}

// second solution
function phoneNumberMnemonics(phoneNumber) {
  const dic = {
    1: "1",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: "0",
  };
  let res = [];

  function dfs(i, cur) {
    if (i === phoneNumber.length) {
      res.push(cur.join(""));
    } else {
      for (let d of dic[phoneNumber[i]]) {
        cur.push(d);
        dfs(i + 1, cur);
        cur.pop();
      }
    }
  }
  dfs(0, []);
  return res;
}
