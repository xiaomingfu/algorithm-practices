'''
input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
'''
def shortestCellPath(grid, sr, sc, tr, tc):
  steps = 0
  m, n = len(grid), len(grid[0])
  q = [(sr,sc)]
  grid[i][j] = 2
  while q:
    newq = []
    for i, j in q:
      if i == tr and j == tc:
        return steps
      for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
          grid[a][b] = 2
          newq.append((a,b))
    steps += 1
    q = newq
  return -1