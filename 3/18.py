zh = input()
ts= '1234567890'
for i in range(len(zh)):
    if zh[i] in ts:
        print('Цифра')
        break
else:
    print('Цифр нет')
#Цифр есть,цифр нетю

# put your python code here
zh = input()
count1 = 0
count2 = 0
for i in range(len(zh)):
    if zh[i] == '+':
        count2 += 1
    elif zh[i] == '*':
        count1 += 1
print("Символ + встречается" ,count2 ,"раз")        
print("Символ * встречается", count1 ,"раз")        