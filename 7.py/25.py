import random
def random1():
    qw = list(qwer)
    qw1 = list(qwer)
    s = [' '] * len(qw)
    count = 0
    while True:
        print(s)
        ts = input('Letter? ')
        ts.lower()
        if ts in qw:
            while True:
                qwe = qw.index(ts)
                s.pop(qwe)
                s.insert(qwe,ts)
                qw.pop(qwe)
                qw.insert(qwe,'')
                qw1.remove(ts)
                if ' ' not in s:
                    return "YOU WIN 😭 ༎ຶ‿༎ຶ"
                if ts not in qw1:
                    break
        elif  ts not in qw:
            count += 1
        elif count == 6:
            return 'GAME OVERRRR !!!! HAHAHAHA 😎 (￣▽￣) '     
        elif count < 6:
            return "YOU WIN 😭 ༎ຶ‿༎ຶ "



things= ['Idol','Member','Bias','Biaslist','Visual','TheLeader','Maknae','Year-line','Trainee','Teaser','Comeback','Promotion','Lightstick','Ocean','Netizen','Subgroup','Fandom','Stan','Stuff','Staff','Egye','Fighting','MiniAlbum','SingleAlbum']

nomer = []
for i in range(len(things)):
    nomer.append(i)
a = random.randint(0,len(nomer)-1)
qwer = things[a]
string =''.join(qwer)
print("Welcome to K-POP Hangman !!!!!")
print(*random1(),sep ='')











































