import random
import os
from GG_art import logo

number=random.randint(1,100)
correct=False

print(logo)
print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")
Difficulty=input("choose the difficulty. type 'easy' or 'hard' ")

if Difficulty=='easy':
    lives=10
elif Difficulty=='hard':
    lives=5
else:
    print("invalid input ")
    correct=True

while not correct:
    print(f"you have {lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess > number:
        os.system('clear')
        print(logo)
        print("try lower")
        lives-=1
    elif guess < number:
        os.system('clear')
        print(logo)
        print("try higher")
        lives-=1
    else:
        print("correct answer")
        correct=True
    if lives==0:
        print ("you ran out of attempts")
        print(f"the correct number was {number}")
        correct=True
