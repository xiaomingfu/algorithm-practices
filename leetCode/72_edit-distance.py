# https://leetcode.com/problems/edit-distance/

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def dfs(i, j):
          if i == len(word1) or j == len(word2):
            return len(word1) - i + len(word2) - j
          if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)
          else:
            return min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1)) + 1
        
        return dfs(0,0)