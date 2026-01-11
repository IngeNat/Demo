
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

'''Rock defeats Scissors.
Scissors defeat Paper.
Paper defeats Rock'''

import random
import time
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

should_continue = True    


print("Welcome to Rock-Paper-Scissors Game!\n", flush=True)

time.sleep(2)
print(rock)#0
print(paper)#1
print(scissors)#2
time.sleep(3)
clear()

def game():

    while True:
        user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip()
        if user_choice in ("0","1","2"):
            user_choice=int(user_choice)
            break
        else:
            print("Incorrect input. Try again - type 0, 1 or 2!\n")
            time.sleep(2)
            clear()


    computer_choice = random.randint(0,2)
    choices_list = [rock, paper, scissors]

    def choices():
        
        print(f"You chose: {user_choice}. ")
        print(choices_list[user_choice])
        print(f"Computer chose: {computer_choice}. ")
        print(choices_list[computer_choice])
        print()
        time.sleep(1)


            #remis
    if  user_choice == computer_choice:
            choices()
            print("Remis! Nobody won. ")

        #rock-scissors
    elif user_choice == 0 and computer_choice == 2:
            choices()
            print("You won. ")

        #rock-scissors
    elif user_choice == 2 and computer_choice == 0:
            choices()
            print("Computer won. ")

        #scissors-paper
    elif user_choice == 2 and computer_choice == 1:
            choices()
            print("You won. ")

        #scissors-paper
    elif user_choice == 1 and computer_choice == 2:
            choices()
            print("Computer won. ")

        #paper-rock
    elif user_choice == 1 and computer_choice == 0:
            choices()
            print("You won. ")

        #paper-rock
    elif user_choice == 0 and computer_choice == 1:
            choices()
            print("Computer won. ")
        
        
     
while should_continue:
    game()
    while True:
        restart = input("Would you like to play once more? Type 'yes' or 'no'.\n ").lower().strip()

        if restart == "yes":
            clear()
            break

        elif restart == "no": 
            should_continue == False #change should_continue parameter
            print("Thank you for the game. Goodbye! ")
            time.sleep(4)
            clear()
            exit()

        else:
            print("Incorrect input. Try again - 'yes' or 'no'.\n")
            time.sleep(3)
            clear()


