def isValidSubsequence(array, sequence):
    # Write your code here.
    #O(n) O(1)
  i = 0
  j = 0
  while i < len(array) and j < len(sequence):
    if array[i] == sequence[j]:
      j += 1
    i += 1
  return j == len(sequence)

#second method
def isValidSubsequence(array, sequence):
  i = 0
  for n in array:
    if n == sequence[i]:
      i += 1
    if i == len(sequence):
      break
  return i == len(sequence)