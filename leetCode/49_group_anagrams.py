# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            k = "".join(sorted([c for c in s]))
            d[k].append(s)
        return list(d.values())