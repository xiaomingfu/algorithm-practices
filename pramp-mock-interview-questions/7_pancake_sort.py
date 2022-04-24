# flip(arr, k) -> [4,3,5,6] k = 2 => [5,3,4,6]
# arr[k] -> arr[0]
# start change
# find the max move to end
def flip(arr, k):
  i, j = 0, k
  while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i, j = i + 1, j - 1
    
def pancake_sort(arr):
  for j in range(len(arr) - 1, - 1, -1):
    max_idx = arr.index(max(arr[:j + 1]))
    if max_idx < j:
      flip(arr, max_idx)
      flip(arr, j)
  return arr