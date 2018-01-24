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
letters_guessed = []
random.shuffle(word_bank)
word = word_bank.pop(0)
word = (list(word))
length = len(word)
while lives > 0 and correct is False:
    print(word)
    guess = input("Guess a letter, the word is %s letters long. " % length)
    if guess == letters_guessed:
        print("You already guessed that letter.")
    for index in range(len(word)):
        guess += word
        print(guess.join(word))
        letters_guessed.append(guess)
    elif guess != word:
        lives -= 1
        letters_guessed.append(guess)
    elif guess == word:
        correct = True
        print("You got the word correct! The word was %s." % word)
    print(guess)
    print("You have %s guesses left" % lives)
