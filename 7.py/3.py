zh, ts = input().split()
zh,ts = int(zh),int(ts)
qw = []


for _ in range(zh):
    values = input().split()
    values = [int(_) for _ in values]
    qw.append(values)

ifcode = True
for i in range(zh - 1):
   for j in range(ts):
      if qw[i][j] == qw[i + 1][j]:
         ifcode = False

if ifcode:
  print("YES")
else:
  print("NO")