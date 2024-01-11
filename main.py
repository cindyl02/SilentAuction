from art import logo


def get_name():
    return input("What is your name? ")


def get_bid():
    success = False
    while not success:
        try:
            bid = int(input("What is your bid? $"))
            if bid <= 0:
                print("Bids smaller or equal to zero are not allowed.")
            else:
                return bid
        except ValueError:
            pass


def get_has_bidders():
    return input('Are there any other bidders? Type "yes" or "no"\n').lower()


def run_auction():
    should_continue = True
    bids = {}

    while should_continue:
        name = get_name()
        bids[name] = get_bid()
        has_bidders = get_has_bidders()
        if has_bidders == "no":
            should_continue = False

    highest_bid = 0
    answer = ""
    for name, price in bids.items():
        if price > highest_bid:
            answer = name
            highest_bid = price
    print(f"The winner of the bid is {answer} with a bid of ${highest_bid}")


if __name__ == '__main__':
    print(logo)
    print("Welcome to the Blind Auction Program!")
    run_auction()
