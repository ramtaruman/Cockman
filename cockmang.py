import random
penisnames = ['penis','phallus','member','peepee','mickey','cock','dick','prick','knob','dong','dingling','tool','equipment','boner','meat','shaft','schlong','johnson']
correct_word=random.choice(penisnames)
dashlist=[]
print(correct_word)
for i in range(len(correct_word)):
    dashlist.append("_")
rounds=len(correct_word)+7 
for round in range(len(correct_word)+7):
       
    guess=input().lower()
    for i in range(len(dashlist)):
        if(guess==correct_word[i]):
            dashlist[i]=guess
    print(dashlist)
    --rounds
    if("_") not in dashlist:
        print("you win") 
        exit()
if("_") in dashlist:
    print("you lost")
    exit()

