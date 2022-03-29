# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # scan left to right to remove extra ")"
        # scan right to left to remove extra " ("
        
        res = []
        cnt = 0
        for c in s:
            if c != ")":
                if c == "(":
                    cnt += 1
                res.append(c)
            else:
                if cnt > 0:
                    cnt -= 1
                    res.append(c)
        t = "".join(res[::-1])
        res = []
        cnt = 0
        for c in t:
            if c != "(":
                if c == ")":
                    cnt += 1
                res.append(c)
            else:
                if cnt > 0:
                    cnt -= 1
                    res.append(c)
        return "".join(res[::-1])