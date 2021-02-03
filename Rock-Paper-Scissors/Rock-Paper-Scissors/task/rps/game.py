import random


def get_dic_win(variants):
    wins = {}
    for i, variant in enumerate(variants):
        new_list = variants[i + 1:] + variants[:i]
        wins[variant] = set(new_list[len(new_list) // 2:])

    return wins


game_variants = ["rock", "paper", "scissors"]

scores = {}
file_rat = open("rating.txt", "r")
for line in file_rat:
    player, score = line.split()
    scores[player] = int(score)
file_rat.close()

name = input("Enter your name: ")
print(f"Hello, {name}")
user_score = scores.get(name, 0)

user_variants = input()
if user_variants:
    game_variants = user_variants.split(",")
dict_win = get_dic_win(game_variants)

print("Okay, let's start")

while True:
    user_input = input()
    comp_var = random.choice(game_variants)

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {user_score}")
    elif user_input not in dict_win:
        print("Invalid input")
    elif comp_var in dict_win[user_input]:
        print(f"Well done. Computer chose {comp_var} and failed")
        user_score += 100
    elif user_input in dict_win[comp_var]:
        print(f"Sorry, but computer chose {comp_var}")
    else:
        print(f"There is a draw ({comp_var})")
        user_score += 50
