import math
zh ,ts,qw = input().split()
zh ,ts,qw = int(zh),int(ts),int(qw)
width = math.ceil(zh/qw)
height = math.ceil(ts/qw)
totall = width * height
print(totall)