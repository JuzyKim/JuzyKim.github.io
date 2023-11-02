zh = input()
count1 = 0
count2 = 0
count3 = 0
count4 = 0
j = 'J,j'
i = 'I,i'
c = 'c,C'
h = 'H,h'
for i in range(len(zh)):
    if j in zh:
        count1 += 1
    if i in zh:
        count2 += 1
    if h in zh:
        count3 += 1
    if c in zh:
        count4 += 1
print('J -',count1)
print('I -',count2)
print('H -',count3)
print('C -',count4)   