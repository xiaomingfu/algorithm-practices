// O(nlogn) time; O(1) space
function minimumWaitingTime(queries) {
  queries.sort((a, b) => a - b);
  let total = 0;
  let cur = 0;
  for (let i = 0; i < queries.length; i++) {
    total = total + cur;
    cur = cur + queries[i];
  }
  return total;
}
