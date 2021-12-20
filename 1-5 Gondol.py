import random
beker = int(input("Adj meg egy számot 1 től 5 ig= "))
random = random.randint(1,5)
if beker == random:
    print("Eltaláltad a számot! Most kurva gyorsan menj és rakj lottót.")
if beker > random:
    print("A te számod nagyobb")
if beker < random:
    print("A te számod kisebb")