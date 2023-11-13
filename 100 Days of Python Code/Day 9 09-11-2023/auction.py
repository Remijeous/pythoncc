from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid amount of {highest_bid}")

while not bidding_finished:
    name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid amount: $"))
    bids[name] = bid_amount
    should_continue = input("Is there any other bidders? 'Yes'or 'No' ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\033c", end="")

