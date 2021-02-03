from random import choice
from string import ascii_lowercase

word_list = ['python', 'java', 'kotlin', 'javascript']
secret_word = choice(word_list)
user_letters = set()
attempts = 8
result_word = "-" * len(secret_word)

print("H A N G M A N\n")
while True:
    oper = input('Type "play" to play the game, "exit" to quit:')
    if oper == "exit":
        break
    if oper == "play":
        while True:
            print(result_word)

            letter = input("Input a letter:")
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
            elif letter in user_letters:
                print("You already typed this letter")
            elif letter in secret_word:
                user_letters.add(letter)
                result_word = "".join([c if c in user_letters else "-" for c in secret_word])
            else:
                user_letters.add(letter)
                print("No such letter in the word")
                attempts -= 1

            if not attempts:
                break

            print()

        if result_word == secret_word:
            print("You guessed the word!\nYou survived!\n")
        else:
            print("You are hanged!\n")
