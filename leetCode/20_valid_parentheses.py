# https://leetcode.com/problems/valid-parentheses/

'''
stack, check empty, when pop and append
'''
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for c in s:
            if c in ")]}":
                if not st:
                    return False
                t = st.pop() + c
                if t not in ["{}", "()", "[]"]:
                    return False
            else:
                st.append(c)
        return len(st) == 0