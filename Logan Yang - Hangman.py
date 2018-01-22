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
while lives > 0 and correct is False:
    random.shuffle(word_bank)
    word = word_bank
    print(list(word))
    guess = input("Guess a letter. ")
    if guess != list(word):
        lives -= 1
    elif guess == list(word):
        guess += list(word)
