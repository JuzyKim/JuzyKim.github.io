# + * skolka
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