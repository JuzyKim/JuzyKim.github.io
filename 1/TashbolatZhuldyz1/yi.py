zh = int(input())
f1 = 0
f2 = 1
for i in range(zh):
    f2 = f1 + f2          # присваиваем переменной num2 новое значение суммы этой переменной с предыдущей
    f2 = f2 - f1
print(f1, end='   ')