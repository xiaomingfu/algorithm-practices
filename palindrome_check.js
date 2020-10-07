// O(n) time | O(1) space
function isPalindrome(string) {
  // Write your code here.
  for (let i = 0, j = string.length - 1; i < j; i++, j--) {
    if (string[i] !== string[j]) {
      return false;
    }
  }
  return true;
}
