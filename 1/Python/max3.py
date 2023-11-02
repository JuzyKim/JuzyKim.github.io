n = int(input())
max1 = -1
max2 = 0
max3 = 1
counter = 0
for i in range(1,n + 1):
    ts = int(input())
    if ts > max1:
            max3 = max2
            max2 = max1
            max1 = ts
    elif ts > max2:
        max2 = max1
        max2 = ts
    elif ts > max3:
        max3 = ts
print(max1)
print(max2)
print(max3)
























