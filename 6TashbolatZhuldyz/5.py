zh = input()
gla = "AOYEUIaoyeui"
res = ''
for i in zh:
    if i not in gla:
        if i.isupper():
            res += '.' + i.lower()
        else:
            res += '.' + i
print(res)
