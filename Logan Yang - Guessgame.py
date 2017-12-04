import random
# Logan Yang

number = (random.randint(0, 50))
input("What number am I thinking of? ")
if input == number:
    print("Correct")
elif input <= number:
    print("Incorrect, guess higher")
elif input >= number:
    print("Incorrect, guess lower")
