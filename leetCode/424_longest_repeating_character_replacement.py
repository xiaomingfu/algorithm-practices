#https://leetcode.com/problems/longest-repeating-character-replacement/submissions/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def check(i, j, cnts):
            idx = ord(s[j]) - ord("A")
            maxf = max(cnts)
            if cnts[idx] == maxf:
                maxf += 1
            return (j - i + 1 - maxf) <= k
            
        cnts = [0] * 26
        res = 0
        i, j = 0, 0
        while j < len(s):
            if check(i, j, cnts):
                idx = ord(s[j]) - ord("A")
                cnts[idx] += 1
                j += 1
            else:
                idx = ord(s[i]) - ord("A")
                cnts[idx] -= 1
                i += 1
            res = max(res, j - i)
        return res
        