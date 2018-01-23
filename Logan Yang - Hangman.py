import random
# Logan Yang
# Period 3
'''
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Hide the word (use *)
4. Reveal letters already guessed
5. Create the win condition
'''
word_bank = ["Seoul Dynasty", "Dallas Fuel", "London Spitfire", "San Francisco Shock", "Houston Outlaws",
             "Boston Uprising", "Los Angeles Gladiators", "Los Angeles Valiant", "Florida Mayhem", "New York Excelsor",
             "Philadelphia Fusion", "Shanghai Dragons"]
correct = False
lives = 10
letters_guessed = ""
start = True
while lives > 0 and correct is False:
    if start == True:
        range(1)
        random.shuffle(word_bank)
        word = word_bank.pop(0)
        word = (list(word))
        length = len(word)
        print(length)
        print(word)
        guess = input("Guess a letter, the word is %s letters long. " % length)
        start = False
    if guess == letters_guessed:
        print("You already guessed that letter.")
    if guess == list(word):
        guess += list(word)
        guess += letters_guessed
    elif guess != list(word):
        lives -= 1
        guess += letters_guessed
    if guess == word:
        correct = True
        print("You got the word correct! The word was %s." % word)
    print(guess)
    print("You have %s guesses left" % lives)
