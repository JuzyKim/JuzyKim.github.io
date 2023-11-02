import random

for i in range (0,101) :
    print("Guess the Number game!")
    print("Come up with a number from 1 to 100, and I'll guess it.")

    lw = 1
    hh = 100
    result = 0

    while lw <= hh:
        botguess = random.randint(lw, hh)
        print(f"My guess is {botguess}")

        feck = input("Is my guess ( too high, too low, correct)? ")

        if feck == "correct":
            print(f"I guessed your number in {result} attempts!")
            break
        
        elif feck == "too high":
            hh = botguess + 1
        elif feck == "too low":
            lw = botguess - 1
        else:
            print("Give reasonable feedback:too high, too low, correct.")

        result += 1

    if lw > hh:
        print("I couldn't guess your number. WWWWWWWWWWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWW!")

print(i)