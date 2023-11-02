import random

for i in range (0,101):
    print("Guess the Number game!")
    print("Come up with a number from 1 to 100, and I'll guess it.")

    lw = 1
    hh = 100
    attem = 0

    while lw <= hh:
        bot_guess = random.randint(lw, hh)
        print(f"My guess is {bot_guess}")

        fback = input("Is my guess (too high, too low, or correct)? ")

        if fback == "correct":
            print("HAHAHAHAHAHAHAA! I GUESSED YOUR NUMBER ")
            break
        elif fback == "too high":
            hh = bot_guess - 1
        elif fback == "too low":
            lw = bot_guess + 1
        else:
            print("Give reasonable feedback: 'too high', 'too low', 'correct'.")
    attem += 1

    if lw > hh:
        print("I couldn't guess your number. WWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOOOOOOOOOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWWWWWW!")
print(i)
