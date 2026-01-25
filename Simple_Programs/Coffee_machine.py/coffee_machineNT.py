import time
import os
import sys
from tkinter import N
from cm_data import resources
from cm_data import MENU

Money = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def user_info():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            sys.exit()
        if user_input in ["espresso", "latte", "cappuccino", "report"]:
            return user_input        
        print('Invalid input. Please type "espresso", "latte", "cappuccino" or "report". ')
        time.sleep(5)
        clear()


def report_func(resources, Money):
    print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: $ {Money}\n\n")
    time.sleep(5)  


def processing_func(user_input, MENU, resources):
    for x in MENU[user_input]["ingredients"]:
        resources[x] -= MENU[user_input]["ingredients"][x]
       
    print(f"\nHere's your {user_input} ☕️ Enjoy!")
    time.sleep(6)  
    return resources


def money_process(Money, user_input, resources):

    while True: 
        try:
            quarters = abs(int(input("Please insert coins. \nHow many quarters? ")))
            dimes = abs(int(input("How many dimes? ")))
            nickles = abs(int(input("How many nickles? ")))
            pennies = abs(int(input("How many pennies? ")))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 5 or 10).")
            time.sleep(4) 
            clear()

    money_bank = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    cost = MENU[user_input]["cost"]

    if money_bank >= cost:
        change = round(money_bank - cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
            time.sleep(4)
        Money += cost
        resources = processing_func(user_input, MENU, resources)
    else:
        print("Sorry that's not enough money. Money refunded.")
        time.sleep(4)
   
    return Money, resources


def ingredients_loop(resources, MENU, ingredients, money_process, user_input, Money):

    can_make = True
    for x in ingredients:
        if x in resources and resources[x] >= ingredients[x]:
            continue
        else:
            print(f"Sorry, there is not enough {x}")
            time.sleep(4)
            can_make = False
            break

    if can_make:
        Money, resources = money_process(Money, user_input, resources)
       
    return Money, resources


while True:
    clear()  #each loop: new screen
    user_input = user_info()

    if user_input == "report":
        report_func(resources, Money)
    elif user_input in ["espresso", "latte", "cappuccino"]:
        ingredients = MENU[user_input]["ingredients"]
        Money, resources = ingredients_loop(resources, MENU, ingredients, money_process, user_input, Money)
    elif user_input == "off":
        sys.exit()
    else:
        print("Incorrect input. Please try again!")
        time.sleep(3)
