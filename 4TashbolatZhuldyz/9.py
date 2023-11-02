zh = input()
ts = zh.capitalize()
for i in range(len(zh)):
    if zh.capitalize() in zh[i]:
        print(zh.replace(ts ,'BURGER'))