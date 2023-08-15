def display_board(board):
    """
    Display the current state of the game board.
    
    Parameters:
    - board (list of lists): The game board represented as a 2D list.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 3))

def get_board_size():
    """
    Prompt the user to input the desired size for the game board.
    
    Returns:
    - int: The selected size for the board.
    """
    while True:
        try:
            size = int(input("Enter board size (e.g., 3 for 3x3, 4 for 4x4, etc.): "))
            if size >= 3:  # Minimum size of 3x3 for the game
                return size
            else:
                print("Please enter a size of 3 or greater.")
        except ValueError:
            print("Please enter a valid number.")

def create_board(size):
    """
    Create a game board of the specified size filled with numbers.
    
    Parameters:
    - size (int): The size of the board.
    
    Returns:
    - list of lists: The created game board.
    """
    return [[str(i * size + j + 1) for j in range(size)] for i in range(size)]

def player_move_dynamic(board, player_symbol):
    """
    Get the next move from the current player and update the board.
    
    Parameters:
    - board (list of lists): The current game board.
    - player_symbol (str): The symbol ('X' or 'O') of the current player.
    
    Returns:
    - list of lists: The updated game board.
    """
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

def check_win(board, player_symbol):
    """
    Check if the current player has won the game.
    
    Parameters:
    - board (list of lists): The current game board.
    - player_symbol (str): The symbol ('X' or 'O') of the current player.
    
    Returns:
    - bool: True if the player has won, False otherwise.
    """
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

def check_tie(board):
    """
    Check if the game has ended in a tie.
    
    Parameters:
    - board (list of lists): The current game board.
    
    Returns:
    - bool: True if the game is a tie, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

def tic_tac_toe_interactive():
    """
    Run the interactive Tic Tac Toe game. The function handles the game loop, player switches,
    and checks for game termination conditions.
    """
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

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Note for GitHub users: To start the game, uncomment the line below and run the script.
# tic_tac_toe_interactive()

