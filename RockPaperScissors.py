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
Img=[rock,paper,scissors]

H=input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n" )

if int(H)>2:
    print("Invalid number you lose")

else:
    print(Img[int(H)])
    M=random.randint(0,2)
    print(f"Computer Chose:{Img[M]}")

    M=str(M)

    if H==M:
        print('tie')
    elif H=='0' and M=='2' or H=='2'and M=='1' or H=='1'and M=='0':
        print('You Win!!!!')
    else:
        print ('You Lose')
