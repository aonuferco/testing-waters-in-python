# GW

BOARD = ["-"] * 9

GAME_STILL_GOING = True

WINNER = None

CURRENT_PLAYER = "X"


# functions

def play_game():
    display_board()

    while GAME_STILL_GOING:
        handle_player(CURRENT_PLAYER)

        check_if_game_over()
        flip_player()

    if WINNER == "X":
        print("Player X won!")
    elif WINNER == "O":
        print("Player O won!")
    elif WINNER is None:
        print("It's a tie!")


def display_board():
    print()
    print(BOARD[0:3])
    print(BOARD[3:6])
    print(BOARD[6:9])
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(positions[0:3])
    print(positions[3:6])
    print(positions[6:9])
    return


def handle_player(player):
    print(player + "'s turn")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1

        if BOARD[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    BOARD[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_if_tie():
    global GAME_STILL_GOING
    if "-" not in BOARD:
        GAME_STILL_GOING = False


def check_for_winner():
    global WINNER

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        WINNER = row_winner
    elif column_winner:
        WINNER = column_winner
    elif diagonal_winner:
        WINNER = diagonal_winner
    else:
        WINNER = None


def check_rows():
    global GAME_STILL_GOING

    if BOARD[0] == BOARD[1] == BOARD[2] != "-":
        GAME_STILL_GOING = False
        return BOARD[0]
    elif BOARD[3] == BOARD[4] == BOARD[5] != "-":
        GAME_STILL_GOING = False
        return BOARD[3]
    elif BOARD[6] == BOARD[7] == BOARD[8] != "-":
        GAME_STILL_GOING = False
        return BOARD[6]
    else:
        return None


def check_columns():
    global GAME_STILL_GOING

    if BOARD[0] == BOARD[3] == BOARD[6] != "-":
        GAME_STILL_GOING = False
        return BOARD[0]
    elif BOARD[1] == BOARD[4] == BOARD[7] != "-":
        GAME_STILL_GOING = False
        return BOARD[1]
    elif BOARD[2] == BOARD[5] == BOARD[8] != "-":
        GAME_STILL_GOING = False
        return BOARD[2]
    else:
        return None


def check_diagonals():
    global GAME_STILL_GOING

    if BOARD[0] == BOARD[4] == BOARD[8] != "-":
        GAME_STILL_GOING = False
        return BOARD[0]
    elif BOARD[2] == BOARD[4] == BOARD[6] != "-":
        GAME_STILL_GOING = False
        return BOARD[2]
    else:
        return None


def flip_player():
    global CURRENT_PLAYER

    if CURRENT_PLAYER == "X":
        CURRENT_PLAYER = "O"
    else:
        CURRENT_PLAYER = "X"

    return


# start

#play_game()
