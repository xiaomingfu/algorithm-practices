def array_of_array_products(arr):
  '''
  two pointer
  '''
  if len(arr) <= 1:
    return []

  res = []
  for i in range(len(arr)):
    t = 1
    j, k = i, i
    while j > 0:
      t *= arr[j - 1]
      j -= 1
    while k < len(arr) - 1:
      t *= arr[k + 1]
      k += 1
    res.append(t)
  return res