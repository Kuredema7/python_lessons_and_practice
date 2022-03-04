from os import system

def get_highest_bid_value(bid_values):
    highest_value = 0
    winner = ''
    for bidder in bid_values:
        bid_val = bid_values[bidder]
        if bid_val > highest_value:
            highest_value = bid_val
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_value}")



bidders_dict = {}

is_there_bidders = True

while is_there_bidders:
    name = input('What is your name?: ')
    bid = int(input("What's your bid? $"))

    bidders_dict[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    system('cls')

    if choice == 'no':
        is_there_bidders = False
        get_highest_bid_value(bidders_dict)