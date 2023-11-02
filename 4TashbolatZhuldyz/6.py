zh = input()
count1 = 0
for i in range(len(zh)):
    if '>>-->' in zh :
        count1 += 1
    elif '<--<<' in zh: 
        count1 += 1
print(count1)