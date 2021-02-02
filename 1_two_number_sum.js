// solution 1
// o(nlog(n)) time | o(1) space
function twoNumberSum(array, targetSum) {
  // Write your code here.
  array.sort((a, b) => a - b);
  for (let i = 0, j = array.length - 1; i < j; ) {
    if (array[i] + array[j] > targetSum) {
      j--;
    } else if (array[i] + array[j] < targetSum) {
      i++;
    } else {
      return [array[i], array[j]];
    }
  }
  return [];
}

// solution 2
// O(n^2) time | O(1) space
function twoNumberSum(array, targetSum) {
  // Write your code here.
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (targetSum === array[i] + array[j]) {
        return [array[i], array[j]];
      }
    }
  }
  return [];
}

//   solution 3
// 	O(n) time, O(n) space
function twoNumberSum(array, targetSum) {
  let dic = {};

  for (let num of array) {
    let remain = targetSum - num;
    if (dic[remain]) {
      return [remain, num];
    }
    dic[num] = true;
  }
  return [];
}
