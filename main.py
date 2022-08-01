from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
list_of_the_bidders = []
Continue_of_the_action = True 
while Continue_of_the_action:
    new_dict = {}
    name = input("What is your name?")
    bid_amount = int(input("What's your bid? $"))
    other_biders = input("Are there any other bidders? 'yes' or 'no'").lower()
    clear()
    new_dict["name"] = name
    new_dict["bid_amount"] = bid_amount
    list_of_the_bidders.append(new_dict)
    if other_biders == 'no':
        Continue_of_the_action = False
biggest_amount = 0
winner_name = ""
for bidder in list_of_the_bidders:
    if bidder["bid_amount"]>biggest_amount:
        biggest_amount = bidder["bid_amount"]
        winner_name = bidder["name"]
print(f'The winner is {winner_name} with a bid of ${biggest_amount}')
            
    