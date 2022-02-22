# https://leetcode.com/problems/valid-anagram/

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return "".join(sorted([c for c in s])) == "".join(sorted([c for c in t]))
        
        # arr = [0] * 26
        # for c in s:
        #     arr[ord(c) - ord("a")] += 1
        # for c in t:
        #     arr[ord(c) - ord("a")] -= 1
        # return all((c == 0 for c in arr))
        
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        return all((v == 0 for v in d.values()))