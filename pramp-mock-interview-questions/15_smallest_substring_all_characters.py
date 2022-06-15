'''
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"
'''
from collections import defaultdict
def get_shortest_unique_substring(arr, str):
  i, j = 0, 0
  cnt = defaultdict(int)
  s, e = -1, len(str)
  arr_ = set(arr)
  While True:
    if all(cnt[c] > 0 for c in str[i:j + 1]):
      i += 1
    else:
      if j == len(str):
        break
      else:
        w = str[j]
        if w in arr_:
          j += 1
          cnt[str[j]] += 1
    if all(cnt(c) > 0 for c in str[i: j + 1]):
      if (j - i) < (e - s):
        s, e = i ,j
  return str[s:e]
