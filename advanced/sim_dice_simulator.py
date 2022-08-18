import random


while True:
    input('enter to roll dice 🎲') # fake input to simulate user input    
    roll = random.randint(1, 6)
    print('You rolled dice and got 🎲: ',roll)
    if roll == 1:
        print('💀You lose!💀')
        break
    elif roll == 6:
        print('👑You win!👑')
        break
    else:
        print('Keep rolling...')