def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_move(board, player_symbol):
    valid_move = False
    while not valid_move:
        try:
            move = int(input(f"{player_symbol}'s move (1-9): "))
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
                return False
    return True

def tic_tac_toe_interactive():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'

    for _ in range(9):
        display_board(board)
        board = player_move(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"{current_player} wins!")
            return
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print("It's a tie!")

# When you run this in your local environment, call the function to start the game
tic_tac_toe_interactive()
