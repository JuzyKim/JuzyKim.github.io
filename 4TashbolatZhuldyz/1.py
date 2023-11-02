zh = int(input())
for i in range(zh):
    for j in range(23):
        if (i == 0 or i == zh-1 or j == 0 or j == 22): 
            print('*', end='') 
        else: 
            print(' ', end='')
    print()