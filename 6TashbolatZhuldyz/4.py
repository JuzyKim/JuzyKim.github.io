zh ,ts,qw = input().split()
zh ,ts,qw = int(zh),int(ts),int(qw)
width = -(-zh//qw)
height = -(-ts//qw)
totall = width * height
print(totall)