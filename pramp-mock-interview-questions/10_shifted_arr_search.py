def shifted_arr_search(shiftArr, num):
  def bs(i, j):
    if i > j:
      return -1
    m = (i + j) // 2
    if shiftArr[m] > num:
      return bs(i, m - 1)
    elif shiftArr[m] == num:
      return m
    else:
      return bs(m + 1, j)
  
  def helper(i, j):
    if i > j:
      return -1
    m = (i + j) // 2
    
    if shiftArr[m] == num:
      return m
    
    if shiftArr[i] <= shiftArr[m - 1]:
      l = bs(i, m - 1)
      if l != -1:
        return l
      return helper(m + 1, j)
    else:
      r = bs(m + 1, j)
      if r != -1:
        return r
      return helper(i, m - 1)
  
  return helper(0, len(shiftArr) - 1)