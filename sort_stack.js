function sortStack(stack) {
  if (stack.length === 0) {
    return stack;
  }
  const top = stack.pop();
  sortStack(stack);
  insertSortStack(stack, top);
  return stack;
}

function insertSortStack(stack, top) {
  if (stack.length === 0 || stack[stack.length - 1] <= top) {
    stack.push(top);
    return;
  }
  const needSort = stack.pop();
  insertSortStack(stack, top);
  stack.push(needSort);
}
