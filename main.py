def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Let's create an initial game board and display it
initial_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
display_output = display_board(initial_board)
# Simulating the player's move with the input provided
player_symbol = 'X'  # Let's assume player X is making the move

def player_move_simulation(board, player_symbol, simulated_input):
    valid_move = False
    while not valid_move:
        try:
            move = simulated_input  # Using the provided input instead of calling input()
            if 1 <= move <= 9:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] not in ['X', 'O']:
                    board[row][col] = player_symbol
                    valid_move = True
                else:
                    print("Cell already taken. Choose another cell.")
            else:
                print("Invalid move. Choose a number between 1-9.")
        except ValueError:
            print("Please enter a valid number between 1-9.")
    return board

def check_win(board, player_symbol):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player_symbol for cell in board[i]]) or \
           all([board[j][i] == player_symbol for j in range(3)]):
            return True
            
    if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
        return True
    if board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
        return True
        
    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False  # The board still has empty cells
    return True



updated_board = player_move_simulation(initial_board, player_symbol, 2)
display_output = display_board(updated_board)
