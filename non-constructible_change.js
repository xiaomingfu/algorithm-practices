function nonConstructibleChange(coins) {
  // Write your code here.
  if (coins.length === 0) {
    return 1;
  }
  coins.sort((a, b) => a - b);
  let sum = 0;
  for (let coin of coins) {
    if (coin > sum + 1) {
      return sum + 1;
    }
    sum += coin;
  }
  return sum + 1;
}
