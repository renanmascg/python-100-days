from secret_auction_art import logo

print(logo)

auction = dict()
continue_auction = True

def find_highest_bidder(bidding_record):
    winner = { "name": '', "bid": 0 }

    for key in bidding_record:
        if auction[key] > winner['bid']:
            winner["name"] = key
            winner["bid"] = auction[key]
    
    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")


while continue_auction:
    name = input("What's your name ?")
    bid = int(input("What's your bid ? $"))

    auction[name] = bid

    continue_answer = input("Are there any other bidders? Type 'yes' or 'no'")

    if continue_answer == 'no':
        continue_auction = False
        find_highest_bidder(auction)



    
