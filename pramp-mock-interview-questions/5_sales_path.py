########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

def get_cheapest_cost(rootNode):
  def dfs(node):
    if len(node.children) == 0:
      return node.cost
    else:
      min_cost = float("inf")
      for n in node.children:
        min_cost = min(min_cost, dfs(n))
      return node.cost + min_cost
  return dfs(rootNode)

# second solution
def get_cheapest_cost(rootNode):
  min_path = float("inf")
  def dfs(node, cur):
    if len(node.children) == 0:
      nonlocal min_path
      min_path = min(node.cost + cur, min_path)
    else:
      for n in node.children:
        dfs(n, cur + node.cost)
  dfs(rootNode, 0)
  return min_path