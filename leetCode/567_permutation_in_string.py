# https://leetcode.com/problems/permutation-in-string/

from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        for i in range(len(s2)):
            need[s2[i]] -= 1
            if need[s2[i]] == 0:
                del(need[s2[i]])
            if i >= len(s1):
                j = i - len(s1)
                need[s2[j]] += 1
                if need[s2[j]] == 0:
                    del(need[s2[j]])
            if len(need) == 0:
                return True
        return False