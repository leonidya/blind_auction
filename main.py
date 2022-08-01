from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
new_dict = {}
Continue_of_the_action = True 
while Continue_of_the_action:
    name = input("What is your name?")
    bid_amount = int(input("What's your bid? $"))
    other_biders = input("Are there any other bidders? 'yes' or 'no'").lower()
    clear()
    new_dict[name] = bid_amount
    if other_biders == 'no':
        Continue_of_the_action = False
highest_amount = 0
winner_name = ""
print(new_dict)
for bidder in new_dict:
    biggest_amount = new_dict[bidder]
    if biggest_amount > highest_amount:
        highest_amount = biggest_amount
        winner_name = bidder
print(f'The winner is {winner_name} with a bid of ${highest_amount}')
            
    