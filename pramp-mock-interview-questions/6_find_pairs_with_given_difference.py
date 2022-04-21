#  arr = [0, -1, -2, 2, 1], k = 1
# [[1, 0], [0, -1], [-1, -2], [2, 1]]

def find_pairs_with_given_difference(arr, k):
  #[x, y]
  # in order of y in arr
  '''
  res = []
  for i in range(len(arr)):
    for j in range(len(arr)):
      if i != j and arr[j] - arr[i] == k:
        res.append([arr[j], arr[i]])
  return res
  '''
  if not len(arr):
    return []
  s = set(arr)
  res = []
  for y in arr:
    x = y + k
    if x in s:
      res.append([x, y])
  return res