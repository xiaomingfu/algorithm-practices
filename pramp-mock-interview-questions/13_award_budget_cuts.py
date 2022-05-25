# - sum(N) < new_B
# e = cap for e in N if e > cap
# least change
'''
grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
-> 47

cap
cap for n in sorted(grantsArray) if n > cap
cap * (len(G) - cnt(n < cap)) + sum(n < cap) = newB
'''
def find_grants_cap(grantsArray, newBudget):
  t = 0
  for i, g in enumerate(grantsArray.sort()):
    if g >= cap:
      g = cap
    else:
      t += g
      cap = min((newBudget - t) / (len(grantsArray) - i - 1), cap)