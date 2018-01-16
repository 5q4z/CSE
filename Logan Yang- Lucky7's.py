import random
# Logan Yang
# Period 3
round = 0
money = 15
zero = False
high = 0
while money > 0 and zero is False:
    d1 = (random.randint(1, 6))
    d2 = (random.randint(1, 6))
    round += 1
    if d1 + d2 == 7:
        money += 4
    elif d1 + d2 != 7:
        money -= 1
    if high < money:
        high = money
        num = round
    if money == 0:
        zero is True
        print("You have played %s rounds and lost." % round)
        print("You should've stopped at round %s where you had %s dollars." % (num, high))
