function tournamentWinner(competitions, results) {
  let points = {};
  let highest = 0;
  let res = "";
  for (let i = 0; i < results.length; i++) {
    let winner = results[i] ? competitions[i][0] : competitions[i][1];
    points[winner] = points[winner] + 3 || 3;
    if (highest < points[winner]) {
      highest = points[winner];
      res = winner;
    }
  }
  return res;
}
