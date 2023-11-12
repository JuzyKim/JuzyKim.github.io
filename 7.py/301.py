def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 70:
        return 4
    elif grade >= 50: 
        return 3
    elif grade >= 20:
        return 2
    else:
        return 1

# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))