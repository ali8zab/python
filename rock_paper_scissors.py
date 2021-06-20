import random

choices = ["rock", "paper", "scissors"]

def answer():
    answer1 = input("your choice: ")
    answer2 = random.choice(choices)
    if answer1 == answer2:
        print("system has chosen the same!")
        print("It's a Draw!!!")
    elif answer1 == 'paper' and answer2 == 'rock':
        print("system: rock")
        print("you have won!!!")
    elif answer1 == 'paper' and answer2 == 'scissors':
        print("system: scissors")
        print("you have lost!!!")
    elif answer1 == 'rock' and answer2 == 'scissors':
        print("system: scissors")
        print("you have won!!!")
    elif answer1 == 'rock' and answer2 == 'paper':
        print("system: paper")
        print("you have lost!!!")
    elif answer1 == 'scissors' and answer2 == 'paper':
        print("system: paper")
        print("you have won!!!")
    elif answer1 == 'scissors' and answer2 == 'rock':
        print("system: rock")
        print("you have lost!!!")

answer()
    