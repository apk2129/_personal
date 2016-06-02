import random

def rollDice():

    roll = random.randint(1, 100)
    print(roll)
    if   roll == 100    : return False
    elif roll<50        : return False
    else                : return True

def simple_bettor(funds, initial_wager, wager_count):

    value = funds
    wager = initial_wager

    current_wager = 0

    while current_wager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        current_wager  += 1
    return value

if __name__=="__main__":
    print()
    print("---------->", simple_bettor(1000, 100, 100))
