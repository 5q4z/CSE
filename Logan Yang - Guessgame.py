import random
# Logan Yang

a = (random.randint(1, 50))
b = input("What number am I thinking of? ")
if b == str(a):
    print("Correct! Good job.")
elif b < str(a):
    print("Incorrect, guess higher.")
elif b > str(a):
    print("Incorrect, guess lower.")
