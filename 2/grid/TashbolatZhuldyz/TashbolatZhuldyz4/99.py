a = int(input())
b = int(input())
for i in range (a, b + 1 ):
    count = 0
    a = i % 2 
    if a != 0:
        count+= a


print( sep =",")