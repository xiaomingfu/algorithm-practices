#input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
# output: [3, 6, 7]

def find_duplicates(arr1, arr2):
  res = []
  m, n = len(arr1), len(arr2)
  i, j = 0, 0
  while i < m and j < n:
    if m > n:
      a, b = 0, len(arr1) - 1
      while a < b:
        m = (a + b) // 2
        if arr1[m] < arr2[j]:
          a = m + 1
        elif arr1[m] > arr2[j]:
          b = m
        else:
          res.append(arr1[m])
          j += 1
          a = m + 1