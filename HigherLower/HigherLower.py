from game_data import data
from HL_art import logo,vs
import os
import random


print(logo)
score=0
wrong=False

B=random.choice(data)

while not wrong:
    A=B
    B=random.choice(data)
    while A==B:
        B=random.choice(data)
    def format_data(A):
        """format the account data into printable format"""
        name=A['name']
        desc=A['description']
        country=A['country']
        return f"{name} a {desc} from {country}"

    def answer(guess,count1,count2):
        ''' takes the user guess and the follower's count and return whether  they got it right or not '''
        if count1>count2:
            return guess=='a'
        else:
            return guess=='b'

    print(f"Compare A:{format_data(A)}")
    print(vs)
    print(f"Against B:{format_data(B)}")
    guess=input("who has more followers? type 'A' or 'B' ").lower()
    count_a=A['follower_count']
    count_b=B['follower_count']
    correct=answer(guess,count_a,count_b)
    os.system('clear')
    print(logo)

    if correct:
        score+=1
        print(f"you 're right. current score {score}")
    else:
        wrong=True
        print(f"sorry, that's wrong. final score {score} ")