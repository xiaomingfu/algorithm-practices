function taskAssignment(k, tasks) {
  const sort_tasks = [...tasks].sort((a, b) => a - b);
  const res = [];
  let dic = {};

  for (let i = 0; i < tasks.length; i++) {
    const t = tasks[i];
    if (t in dic) {
      dic[t].push(i);
    } else {
      dic[t] = [i];
    }
  }

  for (let i = 0; i < k; i++) {
    const t_1 = sort_tasks[i];
    const t_1_idx = dic[t_1].pop();

    const t_2 = sort_tasks[tasks.length - 1 - i];
    const t_2_idx = dic[t_2].pop();

    res.push([t_1_idx, t_2_idx]);
  }

  return res;
}
