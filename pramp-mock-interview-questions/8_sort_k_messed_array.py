# sort_k_messed_array

'''
arr = [1, 2, 3, 4, 5,6, 7, 8, 9, 10], k = 2
1
O:    [0, 2], [0, 3]...
 for i 0 < (j,k) < len(arr)

TC: O(n * k)
SC: O(n)
heap: On(log(n))
'''

import heapq

def sort_k_messed_array(arr, k):
  if k == 0:
    return arr
  h = []
  res = []
  for i, v in enumerate(arr):
    heapq.heappush(h, v)
    if len(h) >= k + 1:
      res.append(heapq.heappop(h))
  while h:
    res.append(heapq.heappop(h))
  return res
'''
def sort_k_messed_array(arr, k):
  if k == 0:
    return arr
  for i in range(len(arr)):
    for j in range(i + 1, i + k + 1):
      if j < len(arr) and arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr
'''

