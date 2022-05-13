"""
Xiaoming, 30min, 2:02 -> 2: 32 
"""
"""
1- "X.X.X.X" 
2- "X" 0-255
3- digit
4- 4 X
5- 00
6- None

eg:
'192.168.0.1'
"0.23.ss.460.ff"
"""
def validateIP(ip):
  
  def check(p):
    if not p.isdigit():
      return False
     
    if p[0] == "0" and len(p) > 1:
      return False
    return 0 <= int(p) <= 255
  
  if not ip:
    return False
  
  parts = ip.split(".")
  if len(parts) != 4:
    return False
  
  for p in parts:
    if not check(p):
      return False
  return True

'''
ip_1 = "01.34.56.1000.aa."
-> ["0","100","256","255"]
->[0,100,254,255]
-> T: O(1), S:(1)
'''
