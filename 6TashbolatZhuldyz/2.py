zh = int(input())
qw = []

for i in range(zh):
    slova = input()
    if len(slova) > 10:
        lenofslova = slova[0] + str(len(slova) - 2) + slova[-1]
        qw.append(lenofslova)
    else :
        qw.append(slova)

for lenofslova in qw:
    print(lenofslova)