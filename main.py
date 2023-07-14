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

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

print(f"Computer chose\n{computer_choice}")

if user_choice == 0 and computer_choice == 2:
  print("You wins!")
elif computer_choice == 0 and user_choice == 2:
  print("You wins!")
elif computer_choice > user_choice:
   print("You lose!")
elif computer_choice == user_choice:
  print("It is a draw")
elif computer_choice < user_choice:
  print("you win!!")
else:
  print("You chose a invalid numeber. You lose")

