# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []
        def bt(cnt_o, cnt_c):
            if cnt_o == cnt_c == n:
                res.append("".join(st))
            if cnt_o < n:
                st.append("(")
                bt(cnt_o + 1, cnt_c)
                st.pop()
            if cnt_c < cnt_o:
                st.append(")")
                bt(cnt_o, cnt_c + 1)
                st.pop()
        bt(0, 0)
        return res