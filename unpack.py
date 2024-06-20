first, last = input("What's your name? ").split(" ")
print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return galleons * 17 * 29 + sickles * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
