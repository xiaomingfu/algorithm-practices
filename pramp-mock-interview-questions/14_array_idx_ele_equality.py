'''
Given a sorted array arr of distinct integers, 
write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. 
Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
'''
def index_equals_value_search(arr):
  i, j = 0, len(arr) - 1
  while i < j:
    m_idx = (i + j) // 2
    if arr[m_idx] < m_idx:
      i = m_idx + 1
    else:
      j = m_idx
  if arr[j] == j:
    return j
  else:
    return -1