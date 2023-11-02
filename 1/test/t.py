k1 = int(input())
c1 = int(input())
k2 = int(input())
c2 = int(input())
k = k2 - k1  
c = c2 - c1 
if -1 <= k <= 1 and -1 <= c <= 1:
    print('YES')
else:
    print('NO')