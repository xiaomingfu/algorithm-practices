# https://leetcode.com/problems/evaluate-reverse-polish-notation/

import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        st = []
        for token in tokens:
            if token in "+-*/":
                b, a = st.pop(), st.pop()
                c = operations[token](a,b)
                st.append(c)
            else:
                st.append(int(token))
        return st.pop()