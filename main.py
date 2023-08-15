# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'

def display_board(board):
    """
    Display the current state of the game board with consistent cell width.
    
    Parameters:
    - board (list of lists): The game board represented as a 2D list.
    """
    size = len(board)
    max_width = len(str(size * size))
    for row in board:
        formatted_row = [f"{cell:^{max_width}}" for cell in row]
        print(" | ".join(formatted_row))
        print("-" * (size * (max_width + 2)))

def get_board_size():
    """
    Prompt the user to input the desired size for the game board.
    
    Returns:
    - int: The selected size for the board.
    """
    while True:
        try:
            size = int(input("Enter board size (e.g., 3 for 3x3, 4 for 4x4, etc.): "))
            if size >= 3:
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

def get_user_input(prompt, valid_choices):
    """
    Get validated input from the user.
    
    Parameters:
    - prompt (str): Message to display to the user.
    - valid_choices (list): List of valid inputs.
    
    Returns:
    - str: Validated user input.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        print(f"Invalid input. Please choose from {', '.join(valid_choices)}.")

def is_win_condition(cells, player_symbol):
    """
    Check if the given cells form a win for the player.
    
    Parameters:
    - cells (list): List of cells (either row, column, or diagonal).
    - player_symbol (str): The player's symbol ('X' or 'O').
    
    Returns:
    - bool: True if the cells form a win condition, False otherwise.
    """
    return all(cell == player_symbol for cell in cells)

def check_win(board, player_symbol):
    """
    Check if the current player has won the game.
    
    Parameters:
    - board (list of lists): The current game board.
    - player_symbol (str): The player's symbol ('X' or 'O').
    
    Returns:
    - bool: True if the player has won, False otherwise.
    """
    size = len(board)
    
    for i in range(size):
        if is_win_condition(board[i], player_symbol) or \
           is_win_condition([board[j][i] for j in range(size)], player_symbol):
            return True

    if is_win_condition([board[i][i] for i in range(size)], player_symbol) or \
       is_win_condition([board[i][size - 1 - i] for i in range(size)], player_symbol):
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
    return all(cell in [PLAYER_X, PLAYER_O] for row in board for cell in row)

def player_move_dynamic(board, player_symbol):
    """
    Get the next move from the current player and update the board.
    
    Parameters:
    - board (list of lists): The current game board.
    - player_symbol (str): The symbol ('X' or 'O') of the current player.
    
    Returns:
    - list of lists: The updated game board.
    """
    size = len(board)
    valid_choices = [str(i) for i in range(1, size*size + 1)]
    
    valid_move = False
    while not valid_move:
        move = get_user_input(f"{player_symbol}'s move (1-{size*size}): ", valid_choices)
        move = int(move)
        
        row, col = (move - 1) // size, (move - 1) % size
        if board[row][col] not in [PLAYER_X, PLAYER_O]:
            board[row][col] = player_symbol
            valid_move = True
        else:
            print("Cell already taken. Choose another cell.")
    return board

def tic_tac_toe_interactive():
    """
    Run the interactive Tic Tac Toe game. The function handles the game loop, player switches,
    and checks for game termination conditions.
    """
    size = get_board_size()
    board = create_board(size)
    current_player = PLAYER_X

    for _ in range(size * size):
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
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Note for GitHub users: To start the game, uncomment the line below and run the script.
tic_tac_toe_interactive()

