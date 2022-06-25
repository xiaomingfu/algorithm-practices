https://leetcode.com/problems/lru-cache/

class DLNode:
  def __init__(self,key:int,value:int):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None
  
class LRUCache:
  def __init__(self, capacity:int):
    self.capacity = capacity
    self.d = {}
    self.head = DLNode(0,0)
    self.tail = DLNode(0,0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key:int) -> int:
    if key in self.d:
      node = self.d[key]
      self._remove(node)
      self._add(node)
      return node.value
    return -1

  def put(self, key:int, value:int) -> None:
    if key in self.d:
      self._remove(self.d[key])
    node = DLNode(key, value)
    self._add(node)
    self.d[key] = node
    if len(self.d) > self.capacity:
      node = self.head.next
      self._remove(node)
      del(self.d[node.key])
  
  def _add(self, node:DLNode) -> None:
    node.prev = self.tail.prev
    node.next = self.tail
    self.tail.prev.next = node
    self.tail.prev = node
  def _remove(self, node:DLNode) -> None:
    node.prev.next = node.next
    node.next.prev = node.prev