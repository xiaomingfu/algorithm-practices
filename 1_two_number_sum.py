# solution 1
# onlogn time | o1 space
def twoNumberSum(array, targetSum):
  array.sort()
  i = 0
  j = len(array) - 1
  while i < j:
    if array[i] + array[j] > targetSum :
      j -= 1
    elif array[i] + array[j] < targetSum:
      i += 1
    else:
      return [array[i], array[j]]
  return []

# solution 2
# On^2 time | O1 space
def twoNumberSum(array, targetSum) :
  # Write your code here.
  for i in range(len(array) - 1):
    for j in range(i + 1, len(array)) :
      if targetSum == array[i] + array[j]:
        return [array[i], array[j]]
  return []


#   solution 3
# 	On time, On space
def twoNumberSum(array, targetSum) :
  dic = {}
  for num in array :
    remain = targetSum - num
    if remain in dic:
      return [remain, num]
    else:
      dic[num] = True
  return []

# return index of two num
def twoNumberSum(array, targetSum) :
  dic = {}
  for i, n in enumerate(array):
    diff = targetSum - n
    if diff in dic:
      return [i, dic[diff]]
    dic[n] = i