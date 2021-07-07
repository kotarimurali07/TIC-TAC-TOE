# preparing a board
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

game_is_still_going = True
winner = None
current_player = "X"


def display_board():
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])


def play_game():
    global winner
    global game_is_still_going
    global current_player
    display_board()
    while game_is_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won ")
    else:
        print("tie")


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


def check_if_game_over():
    check_if_game_win()
    check_if_game_tie()


def check_if_game_tie():
    global board
    global game_is_still_going
    if "_" not in board:
        game_is_still_going = False
    return


def check_if_game_win():
    global winner
    row_winner = check_row_win()
    column_winner = check_column_win()
    diagonal_winner = check_diagonal_win()
    if row_winner:
        winner = row_winner
    if column_winner:
        winner = column_winner
    if diagonal_winner:
        winner = diagonal_winner


def check_row_win():
    global board
    global game_is_still_going
    row_one = board[0] == board[1] == board[2] != "_"
    row_two = board[3] == board[4] == board[5] != "_"
    row_three = board[6] == board[7] == board[8] != "_"
    if row_one or row_two or row_three:
        game_is_still_going = False
    if row_one:
        return board[0]
    if row_two:
        return board[3]
    if row_three:
        return board[6]


def check_column_win():
    global board
    global game_is_still_going
    column_one = board[0] == board[3] == board[6] != "_"
    column_two = board[1] == board[4] == board[7] != "_"
    column_three = board[3] == board[5] == board[8] != "_"
    if column_one or column_two or column_three:
        game_is_still_going = False
    if column_one:
        return board[0]
    if column_two:
        return board[1]
    if column_three:
        return board[3]


def check_diagonal_win():
    global board
    global game_is_still_going
    diagonal_one = board[0] == board[4] == board[8] != "_"
    diagonal_two = board[2] == board[4] == board[6] != "_"
    if diagonal_one or diagonal_two:
        game_is_still_going = False
    if diagonal_one:
        return board[0]
    if diagonal_two:
        return board[2]


def handle_turn(player):
    global board
    print(player + "'S turn.")
    user_input = input("Choose position from 1-9 : ")
    while user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        user_input = input("Invalid input . Choose position from 1-9 : ")
    user_input = int(user_input) - 1
    while board[user_input] != "_":
        break

    board[user_input] = player
    display_board()


play_game()
