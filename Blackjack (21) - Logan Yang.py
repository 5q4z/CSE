import random
# Logan Yang
# Period 3


bet = True
while bet is True:
    c1 = (random.randint(1, 10))
    c2 = (random.randint(1, 10))
    c3 = (random.randint(1, 10))
    print(c1 + c2)
    if c1 + c2 <= 21:
        hit = input("Hit? ")
        bet = False