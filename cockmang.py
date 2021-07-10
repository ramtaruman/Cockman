import random
penisnames = ['penis','phallus','member','peepee','mickey','cock','dick','prick','knob','dong','dingling','tool','equipment','boner','meat','shaft','schlong','johnson']
correct_word=random.choice(penisnames)
dashlist=[]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(correct_word)
for i in range(len(correct_word)):
    dashlist.append("_")
rounds=5 
correct=False
for round in range(len(correct_word)+7):
    correct=False   
    guess=input().lower()
    for i in range(len(dashlist)):
        if(guess==correct_word[i]):
            dashlist[i]=guess
            correct=True
    if(correct==False):
        rounds-=1
    print(dashlist)
    
    print("Remaining lives: ",rounds)
    if(not(rounds>0)):
        print("you lost")
        exit()
    if("_") not in dashlist:
        print("you win") 
        exit()
if("_") in dashlist:
    print("you lost")
    exit()

