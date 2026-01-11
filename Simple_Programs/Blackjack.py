import random
import time
import os


def ace_change(your_cards_deck_sum, your_cards_deck):
        if your_cards_deck_sum > 21 and 11 in your_cards_deck:
                your_cards_deck[your_cards_deck.index(11)] = 1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
        your_cards_deck = []
        computer_cards_deck = []
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
        if start != "y":
                print("Thank you for the game. Goodbye! ")
                time.sleep(4)
                clear()
                break

        your_initial_cards = random.sample(cards,2)
        your_cards_deck.extend(your_initial_cards)
        your_cards_deck_sum = sum(your_cards_deck)

        print (f"     Your cards: {your_initial_cards}, current score: {your_cards_deck_sum} ")
        computer_choice = random.choice(cards)
        computer_cards_deck.append(computer_choice)

        print(f"     Computer's first choice: {computer_choice} ")

        if your_cards_deck_sum == 21:
                print("\nBlackJack! You won. ")
                time.sleep(5)
                clear()
                break


        while True:
                another_card = input("Type 'y' to pick another card, type 'n' to pass: \n ")
                if another_card == "y":
                        your_next_card = random.choice(cards)
                        your_cards_deck.append(your_next_card)
                        your_cards_deck_sum = sum(your_cards_deck)
                        ace_change(your_cards_deck_sum, your_cards_deck)
                        your_cards_deck_sum = sum(your_cards_deck)
        
                        print (f"     Your cards: {your_cards_deck}, current score: {your_cards_deck_sum} ")
        
                        if your_cards_deck_sum > 21:
                                print("\nSum of your cards higher than 21. You lose! ")
                                time.sleep(5)
                                clear()
                                break
                        elif your_cards_deck_sum == 21:
                                print (f"     Your cards: {your_cards_deck}, current score: {your_cards_deck_sum} ")
                                print("\nSum of your cards is 21! You won. ")
                                time.sleep(5)
                                clear()
                                break
                elif another_card == "n":
                        computer_cards_deck_sum = sum(computer_cards_deck)
                        while computer_cards_deck_sum < 17:
                                computer_choice = random.choice(cards)
                                computer_cards_deck.append(computer_choice)
                                computer_cards_deck_sum = sum(computer_cards_deck)
                                ace_change(computer_cards_deck_sum,computer_cards_deck)
                                computer_cards_deck_sum = sum(computer_cards_deck)
                                print (f"     Computer cards: {computer_cards_deck}, current score: {computer_cards_deck_sum} ")
                                time.sleep(4)
                        if computer_cards_deck_sum > 21:
                                print("\nSum of computer's cards is bigger than 21, so you won! ")
                                time.sleep(5)
                                clear()
                                break
                        elif computer_cards_deck_sum == your_cards_deck_sum:
                                print("\nRemis! Nobody won. ")
                                time.sleep(5)
                                clear()
                                break
                        elif computer_cards_deck_sum > your_cards_deck_sum:
                                print("\nSum of computer's cards is bigger than yours cards.Computer won! ")
                                time.sleep(5)
                                clear()
                                break
                        else:
                                print("\nSum of your cards bigger than computer's cards. You won! ")
                                time.sleep(5)
                                clear()
                                break                                   


                else:
                        print ("\nIncorrect input. Try again. ")
                        time.sleep(4)   
                        clear()
                        print (f"     Your cards: {your_cards_deck}, current score: {your_cards_deck_sum} ")
 


        
        
