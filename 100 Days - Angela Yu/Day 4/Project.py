# Game of rock paper scissor
import random

rock = '''
        _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
'''

paper = '''
         _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''

scissor = '''
      _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)

'''
options = [rock, paper, scissor]

choose = int(input("What do you choose? Type 0 for Rock, type 1 for Paper, type 2 for Scissor. \n"))
print(f"You choose \n{options[choose]}")

choice = random.randint(0, 2)
print(f"Computer choose \n{options[choice]}")

if choose == choice:
    print("Game Draw!!")
elif choose == 0 and choice == 2:
    print("You win!!")
elif choose == 1 and choice == 0:
    print("You win!!")
elif choose == 2 and choice == 1:
    print("You win!!")
else:
    print("You lose!!")
