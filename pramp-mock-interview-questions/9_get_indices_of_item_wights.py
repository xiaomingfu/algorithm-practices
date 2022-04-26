from collections import defaultdict
def get_indices_of_item_wights(arr, limit):
  dic = defaultdict(list)
  if len(arr) == 0:
    return []
  for i in range(len(arr) - 1, -1, -1):
    n = arr[i]
    dic[n].append(i)
  for i in range(len(arr) - 1, -1, -1):
    remain = limit - arr[i]
    if remain in dic:
      for idx in dic[remain]:
        if idx != i:
          return [i, idx]

  return []
  

  
'''
[4,4,4] limit 8
4: 2
rem = 4

[2, 1]

12:08 -> 12:38

 arr = [4, 6, 6 10, 15, 16],  lim = 21
 remian 17, 15, 11, 6, 5
 dic = 4:[0], 6:[2, 1],
  res     [3,1],[3,2]
 [3,3,4] arr[i] integer, lim integer

O: return 1 correct answer,  [j, i] j > i, arr[i] + arr[j] == lim

[4,4,1] limit 5
[2,1] 
[2,0]
v ,i -> hash map: k-> arr[i], v-> [i,j]
arr, check diff lim and arr[i] in hashmap
v, [k, j] -> [i, k], [i, j], sort()
i > j -> back
TC -> O(n)
SC -> O(n)
'''