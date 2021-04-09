function balancedBrackets(string) {
  const stack = [];
  const pairs = ["()", "{}", "[]"];
  const brackets = "(){}[]";
  const openBrackets = "([{";
  for (let c of string) {
    if (brackets.indexOf(c) !== -1) {
      if (openBrackets.indexOf(c) !== -1) {
        stack.push(c);
      } else if (stack.length === 0) {
        return false;
      } else {
        const pair = stack.pop() + c;
        if (pairs.indexOf(pair) === -1) {
          return false;
        }
      }
    }
  }
  return stack.length === 0;
}
