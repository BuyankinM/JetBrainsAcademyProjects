def test_win(win_sym):
    test_rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    win = False
    for i, j, k in test_rows:
        if symbols[i] == win_sym and symbols[j] == win_sym and symbols[k] == win_sym:
            win = True
            break
    return win


def print_game():
    print("---------")
    for i in range(3):
        print(f"| {' '.join(symbols[3 * i:3 * (i + 1)])} |")
    print("---------")


symbols = list(" " * 9)
print_game()
cur_sym = "X"

while True:
    user_input = input("Enter the coordinates:").split()
    correct_input = len(user_input) == 2
    if correct_input:
        x, y = user_input

    if (correct_input and (not x.isdigit() or not y.isdigit())) or not correct_input:
        print("You should enter numbers!")
    elif x not in "123" or y not in "123":
        print("Coordinates should be from 1 to 3!")
    else:
        col_ind, row_ind = int(x) - 1, abs(int(y) - 3)
        if symbols[col_ind + row_ind * 3] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            symbols[col_ind + row_ind * 3] = cur_sym
            print_game()
            cur_sym = "O" if cur_sym == "X" else "X"

            X_win = test_win("X")
            O_win = test_win("O")
            draw = not symbols.count(" ")

            if X_win or O_win or draw:
                if X_win:
                    print("X wins")
                elif O_win:
                    print("O wins")
                else:
                    print("Draw")
                break
