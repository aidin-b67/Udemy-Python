# from replit import clear

from art import logo

print(logo)
print("Welcome to the secret auction program.")



bid_list = {}

bidding_finished = False 

#Searching for max bid and winner through loop function

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

    

  
while not bidding_finished:
  def new_input(new_name,new_bid):
    bid_list[new_name] = new_bid
    
  
  new_name = input("What is your name?: ")
  new_bid = int(input("What's your bid?: $"))
  new_input(new_name,new_bid)
  should_continue = input("Are there any other bidder? Type 'yes' or 'no' . ")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bid_list)
#   elif should_continue == 'yes':
#     clear()
  
print(bid_list)

