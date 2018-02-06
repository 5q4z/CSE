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
word_bank = ["seoul dynasty", "dallas fuel", "london spitfire", "san francisco shock", "houston outlaws",
             "boston uprising", "los angeles gladiators", "los angeles valiant", "florida mayhem", "new york excelsor",
             "philadelphia fusion", "shanghai dragons"]
lives = 10
letters_guessed = []
random.shuffle(word_bank)
word = word_bank.pop(0)
word = (list(word))
print("".join(word))
length = len(word)
while lives > 0:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
            lives + 1
    print("".join(output))
    output = input("Guess a letter, the word is %s letters long. " % length)
    if output == word:
        print("You got the word correct! The word was %s." % word)
        exit(0)
    print("You have %s guesses left" % lives)
    if lives == 0:
        print("You are out of guesses, try again.")
        exit(0)
    lives -= 1
