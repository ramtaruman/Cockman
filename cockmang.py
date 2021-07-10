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
game_over=False
print(correct_word)
for i in range(len(correct_word)):
    dashlist.append("_")
rounds=7 
correct=False
while(not(game_over==True)):
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
        game_over=True
        exit()
    if("_") not in dashlist:
        print("you win")
        game_over=True 
        exit()

