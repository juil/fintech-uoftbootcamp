# Rock Paper Scissors

import random 

# Game choices
choices = ['r','p','s']

# Get user input
userhand = input("Rock, paper, scissors!\n[r,p,s]: ")
# Randomly choose computer's hand
aihand = random.choice(choices)

if userhand == aihand:
    print("Tie")
elif (userhand == 'r' and aihand == 's') or (userhand == 's' and aihand == 'p') or (userhand =='p' and aihand == 'r'):
    print("Win")
else:
    print("Lose")
