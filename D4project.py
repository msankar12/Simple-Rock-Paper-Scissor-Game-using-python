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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What number do u want to choose. 0 for Rock or 1 for paper or 2 for sissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(game_images[user_choice])

if user_choice >= 3 or user_choice < 0:
    print("It's an invalid Number")
elif user_choice ==0 and computer_choice == 2:
    print("You wins..")
elif computer_choice == 0 and user_choice ==2:
    print("You lose and Computer Wins..")
elif computer_choice > user_choice:
    print("You win")
elif user_choice > computer_choice:
    print("You Lose and Computer win.")
elif computer_choice == user_choice:
    print("It's a Draw..")

