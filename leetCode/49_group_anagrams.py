# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            k = "".join(sorted([c for c in s]))
            d[k].append(s)
        return list(d.values())

        # second solution
        dic = defaultdict(list)
        for w in strs:
            cnt = [0]*26
            for c in w:
                cnt[ord(c) - ord("a")] += 1
            dic[tuple(cnt)].append(w)
        return dic.values()