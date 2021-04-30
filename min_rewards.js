function minRewards(scores) {
  const rewards = scores.map((s) => 1);
  for (let i = 0; i < rewards.length - 1; i++) {
    if (scores[i] < scores[i + 1]) {
      rewards[i + 1] = rewards[i] + 1;
    }
  }
  for (let i = scores.length - 1; i >= 1; i--) {
    if (scores[i] < scores[i - 1]) {
      rewards[i - 1] = Math.max(rewards[i] + 1, rewards[i - 1]);
    }
  }
  return rewards.reduce((a, b) => a + b);
}
