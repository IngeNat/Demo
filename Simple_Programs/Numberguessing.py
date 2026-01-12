import time
import os
import random
should_continue = True


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def guess_func(attempts, guess_number):
    print(f"You have {attempts} attempts to guess the number.\n ", end="", flush=True)
    while True:
        try:
            for x in range (attempts):
                    user_input = input("Make a guess:\n ")
                    user_guess = int(user_input)
                    
                
                    if user_guess > guess_number and user_guess in range(1,101):
                        print ("Too high")
                    
                        
                    elif user_guess < guess_number and user_guess in range(1,101):
                        print ("Too low")
                     
                        
                    elif user_guess == guess_number:
                        print("Your guess is correct!\n")
                        break
                    else:
                        print("Incorrect input, try again. \n ")

                    attempts_left = attempts - x -1
                    print(f"Attempts left: {attempts_left}")
            else:
                print(f"So sorry! Number not guessed. The correct number was: {guess_number}\n")
            break        
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 10 or 99).")

while should_continue:
    print("Welcome to the Number Guessing Game! \n", end="", flush=True)
    time.sleep(2)
    print("I'm thinking about a number from 1 to 100. \n", end="", flush=True)
    guess_number = random.randint(1,100)
    #print(guess_number)
    time.sleep(2)

    
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
        if difficulty == 'easy':
                
                guess_func(10, guess_number)
                break
        elif difficulty == 'hard':
                
                guess_func(5, guess_number)
                break
        else:
                print ("\nIncorrect input. Try again. ")
                time.sleep(4)   
                clear()
    restart = input("Would you like to play once more? Type 'yes' or 'no'.\n ").lower()
    if restart == "no": 
        should_continue = False #change should_continue parameter
        time.sleep(1)
        print("Thank you for the game. Goodbye!", end="", flush=True)

