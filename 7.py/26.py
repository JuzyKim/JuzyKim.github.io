import random

def random1(qwer):
    qw = list(qwer.lower()) 
    s = [' '] * len(qw)
    count = 0
    i = 0 
    while count < 10:
        print(" ".join(s))
        ts = input('Letter? ').lower() 
        if ts in qw:
            while i < len(qw):
                if qw[i] == ts:
                    s[i] = ts
                    qw[i] = ''
                i += 1
            i = 0  
            if ' ' not in s:
                print(s)
                return "YOU WIN 😭 ༎ຶ‿༎ຶ"
        else:
            count += 1
    print()
    return 'GAME OVER!!!! HAHAHAHA 😎 (￣▽￣)'

things = ['Idol', 'Member', 'Bias', 'Biaslist', 'Visual', 'TheLeader', 'Maknae', 'Year-line', 'Trainee', 'Teaser', 'Comeback', 'Promotion', 'Lightstick', 'Ocean', 'Netizen', 'Subgroup', 'Fandom', 'Stan', 'Stuff', 'Staff', 'Egye', 'Fighting', 'MiniAlbum', 'SingleAlbum']

rraannddoommmm1 = random.choicechoice(things)
print("Welcome to K-POP Hangman !!!!!")
print(random1(rraannddoommmm1))

