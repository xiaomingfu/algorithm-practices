https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # sign
        #0
        # -2^31: -0x80000000
        # 2^31 - 1: 0x7fffffff
        if not x:
          return x
        sign = abs(x) // x
        res = 0
        x = abs(x)
        while x:
          res = res * 10 + x % 10
          x //= 10
        x *= sign
        if x < 0x80000000 or x > 0x7fffffff:
          return 0
        return res