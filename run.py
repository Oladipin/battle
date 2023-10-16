from random import randint


# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 6 for x in range(6)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 6 for i in range(6)]

print("WELCOME TO BATTLESHIP")


def print_board(board):
    print("  A B C D E F")
    print("  +-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
# computer create 3 ships


def create_ships(board):
    for ship in range(3):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Guess Row: ")
    while row not in "123456":
        print('Not an appropriate row. Guess should be between 1-6\n')
        row = input("Guess Row: ")
    column = input("Guess Column: ").upper()
    while column not in "ABCDEF":
        print('Not an appropriate column. Guess should be between A-F\n')
        column = input("Guess column: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 6
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        print_board(HIDDEN_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hurray! It's a HIT")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("Sorry, It's a MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 3:
            print("You win!")
            print("Congratulations! You've sunk the ship")
            break
        print(f"You have {turns} turns left\n")
        if turns == 0:
            print("You ran out of turns")
            print("GAME OVER")
