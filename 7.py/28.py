import random
print("WELCOME TO MY GAME!")
a2pm = "yes"
while a2pm.lower() == "yes":
    me = input("YOUR TURN ( ͡° ͜ʖ ͡°).CHOISE ONE OF THEM :rock ,paper,scissors\n").lower()
    while me not in ["rock", "paper", "scissors"]:
        me = input("ARE SERIOUS!!!\n").lower()
    bot = random.choice(["rock", "paper", "scissors"])
    print("YOU CHOSE"  ,me)
    print("BOT " , bot)
    if me == bot:
        print("OK! FRIENDSHIP WON!!!")
    elif ((me == "rock" and bot == "scissors") or (me == "paper" and bot == "rock") or (me == "scissors" and bot == "paper")):
        print("AHHH! YOU WIN! ಥ_ಥ")
    else:
        print("GAME OVERRR HAHAHAHAHA!!! I WIN (〜￣▽￣)〜")
        
    a2pm = input("DO YOU WANT TO PLAY WITH ME AGAIN? ( ͡ಠ ʖ̯ ͡ಠ) (yes/no)\n").lower()

