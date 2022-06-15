https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      res = []
      if len(digits) == 0:
        return []
      
      letters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
      }

      def bt(i, arr):
        if i == len(digits):
          res.append("".join(arr))
        else:
          c = digits[i]
          for n in letters[c]:
            arr.append(n)
            bt(i + 1, arr)
            arr.pop()

      bt(0, [])
      return res