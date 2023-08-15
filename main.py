def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_board_size():
    while True:
        try:
            size = int(input("Enter board size (e.g., 3 for 3x3, 4 for 4x4, etc.): "))
            if size >= 3:  # Let's assume a minimum size of 3x3 for the game to be meaningful
                return size
            else:
                print("Please enter a size of 3 or greater.")
        except ValueError:
            print("Please enter a valid number.")

def create_board(size):
    return [[str(i * size + j + 1) for j in range(size)] for i in range(size)]


def player_move_dynamic(board, player_symbol):
    valid_move = False
    size = len(board)
    while not valid_move:
        try:
            move = int(input(f"{player_symbol}'s move (1-{size*size}): "))
            if 1 <= move <= size*size:
                row, col = (move - 1) // size, (move - 1) % size
                if board[row][col] not in ['X', 'O']:
                    board[row][col] = player_symbol
                    valid_move = True
                else:
                    print("Cell already taken. Choose another cell.")
            else:
                print(f"Invalid move. Choose a number between 1-{size*size}.")
        except ValueError:
            print(f"Please enter a valid number between 1-{size*size}.")
    return board

# Note: Since this environment is not interactive in the traditional sense, we can't play the game here.
# However, you can replace your 'player_move' function with the 'player_move_dynamic' function in your code
# and then run it in your local Python environment to play the game interactively.

def check_win(board, player_symbol):
    size = len(board)
    
    # Check rows and columns
    for i in range(size):
        if all([cell == player_symbol for cell in board[i]]) or \
           all([board[j][i] == player_symbol for j in range(size)]):
            return True

    # Check main diagonal
    if all([board[i][i] == player_symbol for i in range(size)]):
        return True

    # Check the other diagonal
    if all([board[i][size - 1 - i] == player_symbol for i in range(size)]):
        return True

    return False

    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

def tic_tac_toe_interactive():
    size = get_board_size()
    board = create_board(size)
    current_player = 'X'

    for _ in range(size * size):  # Adjust the game loop for the board size
        display_board(board)
        board = player_move_dynamic(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            return
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

# When you run this in your local environment, call the function to start the game
tic_tac_toe_interactive()
