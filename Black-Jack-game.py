import random





def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards=[]
computer_cards=[]

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculator_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


    
    
# sum_user = calculator_score(user_cards)

print(f"Your cards: {user_cards}, current score: {calculator_score(user_cards)}")
print(f"Computer's first card: {computer_cards[0]}")











user_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

