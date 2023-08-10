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

updated_board = player_move_simulation(initial_board, player_symbol, 2)
display_output = display_board(updated_board)
