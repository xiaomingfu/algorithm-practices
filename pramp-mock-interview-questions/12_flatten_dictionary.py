from types import prepare_class


def flatten_dictionary(dictionary):
  res = {}
  def bt(d, path):
    if type(d) != dict:
      new_k = ".".join(e for e in path if e)
      res[new_k] = d
    else:
      for k in d.keys():
        path.append(k)
        bt(d[k], path)
        path.pop()
  bt(dictionary, [])
  return res