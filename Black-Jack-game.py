import random





def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
 

user_cards=[]
computer_cards=[]

for card in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculator_score(user_cards, computer_cards):
    user_cards_sum = sum(user_cards)
    computer_cards_sum = sum(computer_cards)
    
print(calculator_score())
print(f"Your cards: {user_cards}, current score: {calculator_score(user_cards_sum)}")
print(f"Computer's first card: {computer_cards[0]}")











user_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

