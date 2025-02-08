print("Welcome to the secret aunction app")
def get_highest_bidding_price(biddings):
    winner = ""
    highest_bid = 0
    for bid in biddings:
        bidding_value = biddings[bid]
        if bidding_value > highest_bid:
            highest_bid = bidding_value
            winner = bid
    return f"{winner} wins the bid with ${highest_bid}"

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bids[name] = bid
    print("\n" * 100)
    should_continue = input("Any other bidder? (y/n): ")
    if should_continue == "n": continue_bidding = False



print(get_highest_bidding_price(bids))
