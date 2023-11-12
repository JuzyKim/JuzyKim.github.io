def howtocheck(zh, ts):
  qw = 0
  if a == b:
    qw = 1/2
  elif a > b:
    qw = 1
  else:
    qw = (1/3) * (1 - (b/6))
  return qw
a,b = input().split()
a,b = int(a),int(b)
print(howtocheck(a, b),sep='')