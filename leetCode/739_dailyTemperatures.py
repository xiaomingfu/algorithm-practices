# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, n: List[int]) -> List[int]:
        res = [0] * len(n)
        st = []
        
        for i in range(len(n) - 1, -1, -1):
            while len(st) > 0 and st[-1][0] <= n[i]:
                st.pop()
            st.append((n[i], i))
            if len(st) > 1:
                res[i] = st[-2][1] - i
        return res