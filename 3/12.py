s = 'All you need is love'
if 'love' in s:
    print('💔')
else:
    print('❤️')

s = 'abcdef'
for c in s:
    print(c)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')




# Объявление переменной строки и переменных для счетчика
string = 'bcd+a++++**31415'
plus_count = 0
star_count = 0

# Цикл по строке
for char in string:
    # Проверка, если символ равен +, увеличить счетчик +
    if char == '+':
        plus_count += 1
    # Проверка, если символ равен *, увеличить счетчик *
    elif char == '*':
        star_count += 1

# Вывод результата
print('Символ + встречается', plus_count, 'раз')
print('Символ * встречается', star_count, 'раз')

number = 12
print(bin(number))

