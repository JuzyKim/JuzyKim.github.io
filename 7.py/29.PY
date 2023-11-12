import random
def meguessingbotnumber():
    mnum= random.randint(1, 300)
    print("WELCOME TO MY GAME!!!")
    count = 0
    print("I will choose a number in the range from 1 to 300.And you have to guess my number.")
    while True:
        guess = int(input("Enter your guess: "))
        count += 1
        if guess == mnum:
            print("Well! You guessed my number", mnum, 'in', count, 'attempts ')
            break
        elif guess < mnum:
            print("TOO LOWWWW!")
        elif guess > mnum:
            print("TOO HIGHHHHHH!")

meguessingbotnumber()
