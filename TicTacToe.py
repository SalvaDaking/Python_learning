from platform import system as OS
from os import system as clean

def instructions():
    global name
    '''Prints the instructions of the game'''
    name = input("Hi, what's your name?\n")

    print(f"\nHi {name}, we're going to play Tic Tac Toe. You'll be the 'X' symbol and I'll be the 'O'.")
    print(f"I DO NOT like loosing, specially against a {OS()} user so, mind that if I can't win I'll stop playing, OK?")
    print(f"In that case, you better press 'q' to exit the program ;P")
    input("Now, press 'Enter' when ready!!")

def show_board():
    '''Prints an updated board'''
    if OS() == "Windows":
        clean("cls")
    else:
        clean("clear")

    for lines in board:
        for cell, ind in zip(lines, range(0, 4)):
            if ind < 3:
                print(f'{cell:^3}', end ="")
            else:
                print(f'{cell:^3}')
    print()

def computer_plays():
    '''Computer chooses '''
    global turn
    best_line = None
    ind = None

    matrix_lines = {"line1": board[1][1:], "line2": board[2][1:], "line3": board[3][1:],
                    "column_A": [board[1][1], board[2][1], board[3][1]],
                    "column_B": [board[1][2], board[2][2], board[3][2]],
                    "column_C": [board[1][3], board[2][3], board[3][3]],
                    "left2right": [board[1][1], board[2][2], board[3][3]],
                    "right2left": [board[1][3], board[2][2], board[3][1]]}

    for v, k in zip(matrix_lines.values(), matrix_lines):

        if v.count('O') == 3:
            best_line = "win!"
            show_board()
            print(f"I won!!! I'm smarter than you!!")
        elif (v.count('O') == 2 and v.count("-") == 1) and turn == "computer":
            best_line = v
            ind = best_line.index("-") + 1
            choose_attack(k, ind)
        else:
            if v.count('X') == 3:
                best_line = "ouch!"
                show_board()
                print(f"Wow, {name}!! You're really good at this.")
            elif v.count('X') == 2 and v.count("-") == 1:
                best_line = v
                ind = best_line.index("-") + 1
                choose_defense(k, ind)
            else:
                if board[2][2] == "-" and turn == "computer":
                    board[2][2] = "O"
                    turn = "player"
                    return
                elif board[1][1] == "-" and turn == "computer":
                    board[1][1] = "O"
                    turn = "player"
                    return

    turn = "player"

def choose_defense(best_line, ind):

    if best_line == "line1": board[1][ind] = "O"
    if best_line == "line2": board[2][ind] = "O"
    if best_line == "line3": board[3][ind] = "O"
    if best_line == "column_A": board[ind][1] = "O"
    if best_line == "column_B": board[ind][2] = "O"
    if best_line == "column_C": board[ind][3] = "O"
    if best_line == "left2right": board[ind][ind] = "O"
    if best_line == "right2left":
        if ind == 1: board[1][3] = "O"
        elif ind == 2: board[2][2] = "O"
        else: board[3][1] = "O"

    # print(f"The name of best attack {best_line}")

def choose_attack(best_line, ind):

    if best_line == "line1": board[1][ind] = "O"; return
    if best_line == "line2": board[2][ind] = "O"
    if best_line == "line3": board[3][ind] = "O"
    if best_line == "column_A": board[ind][1] = "O"
    if best_line == "column_B": board[ind][2] = "O"
    if best_line == "column_C": board[ind][3] = "O"
    if best_line == "left2right": board[ind][ind] = "O"
    if best_line == "right2left":
        if ind == 1:
            board[1][3] = "O"
        elif ind == 2:
            board[2][2] = "O"
        else:
            board[3][1] = "O"

    # print(f"The name of best defence {best_line}")

def end_of_game():
    ''' Ends the game'''
    print("\nThanks for playing Tic Tac Toe.")
    input()
    quit()

def player_plays():

    global choice
    global turn
    choice = input(f"{name}, it's your turn. Choose column and line (i.e. A1): ")

    if choice.upper() == 'Q':
        return choice
    elif choice not in combinations:
        print(
            "\nPlease, make sure you type the column first followed by the row number using uppercase letters, i.e. A1.")
        print("Try again! (Columns are A, B or C and rows are 1, 2 or 3.")
        show_board()
        player_plays()
    else:
        if check_board(board[combinations[choice][0]][combinations[choice][1]]):
            board[combinations[choice][0]][combinations[choice][1]] = "X"
            turn = "computer"
        else:
            print(f"\nHey!! Pay attention, {choice} is already occupied.")
            print(f"Take a second and think about it carefully.\n")
            print("I couldn't expect more from a {OS()} user.")
            input(f"Anyway, press 'Enter' when you're ready...")
            show_board()
            player_plays()
    turn = "computer"
    return turn


def check_board(cell):
    '''Checks if the cell is available or already used.'''
    if cell != "-":
        return False
    return True

# Setting the board game and the possible choices.

board = [[' ', 'A', 'B', 'C'],
             ['1', '-', '-', '-'],
             ['2', '-', '-', '-'],
             ['3', '-', '-', '-']]

combinations = {"A1" : (1, 1), "A2": (2, 1), "A3": (3, 1),
                "B1" : (1, 2), "B2": (2, 2), "B3": (3, 2),
                "C1" : (1, 3), "C2": (2, 3), "C3": (3, 3)}

name = None
turn = "player"
if OS() == "Windows":
    clean("cls")
else:
    clean("clear")
instructions()

while True:

    if computer_plays() == "ouch!":
        print("\nThe game is finished!!")
        end_of_game()
    elif computer_plays() == "win!":
        print("\nThe game is finished!!")
        end_of_game()

    if turn == "player":
        show_board()
        player_plays()
    else:
        show_board()
        computer_plays()

    if choice.upper() == "Q":
        end_of_game()
