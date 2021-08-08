import random

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
stage = "-" * len(word)
guesses = set()
attempts = 8
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        while attempts > 0:
            if stage == word:
                print()
                print(stage)
                print("You guessed the word!")
                print("You survived!")
                break
            while True:
                print()
                print(stage)
                guess = input("Input a letter:")
                if len(guess) == 1:
                    if guess.islower():
                        break
                    else:
                        print("Please enter a lowercase English letter")
                else:
                    print("You should input a single letter")
            if guess in guesses:
                print("You've already guessed this letter")
            elif guess in word:
                stage = ""
                guesses.add(guess)
                for char in word:
                    if char in guesses:
                        stage += char
                    else:
                        stage += "-"
            else:
                guesses.add(guess)
                attempts -= 1
                print("That letter doesn't appear in the word")
        else:
            print("You lost!")
    elif menu == "exit":
        break
    print()