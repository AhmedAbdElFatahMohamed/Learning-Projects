import random
import os
from BJ_art import logo


def deal_card():                                      #deal card for player and dealer ace is represented as 11
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def compare(user_score, computer_score):              #compares between the user and dealer scoer
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def calculate_score(cards):                            #calculate the score of the player and dealer
    if sum(cards)==21:
        return 0
    if 11 in cards and sum(cards) >21:                 #if at first hand player gets an 2 aces replace it with 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def play_game():
    player_cards=[]
    Dealer_cards=[]
    game_over=False
    print(logo)

    for _ in range (2):                              #deals 2 card for user and dealer
        player_cards.append(deal_card())
        Dealer_cards.append(deal_card())

    while not game_over:                             #continue the game
        player=calculate_score(player_cards)
        dealer=calculate_score(Dealer_cards)
        print(f"Your cards: {player_cards}\ndealer cards: {Dealer_cards}")
        if player ==0 or dealer ==0 or player >21:
            game_over=True
        else:
            deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if deal == 'y':
                player_cards.append(deal_card())
            else:
                game_over=True

    while dealer != 0 and dealer < 17:
        Dealer_cards.append(deal_card())
        dealer = calculate_score(Dealer_cards)

    print(f"   Your final hand: {player_cards}, final score: {player}")
    print(f"   Computer's final hand: {Dealer_cards}, final score: {dealer}")
    print(compare(player, dealer))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()
