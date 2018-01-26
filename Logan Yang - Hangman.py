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
print(word)
length = len(word)
while lives > 0 and correct is False:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
            print("You already guessed that letter.")
        else:
            output.append("*")
    print(output)
    guess = input("Guess a letter, the word is %s letters long. " % length)
    if guess == list(word):
        guess += list(word)
        guess += letters_guessed
    elif guess != list(word):
        lives -= 0
        letters_guessed.append(guess)
    if guess == word:
        correct = True
        print("You got the word correct! The word was %s." % word)
    print("You have %s guesses left" % lives)
    if lives == 0:
        print("You lost, but you can always try again.")
