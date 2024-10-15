# Quick Tic Tac Toe game
def check_draw(board):
    # take a tic tac toe board, and return if it is a draw
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def check_win(board):
    # take a tic tac toe board, and return who wins 
    # 1 for player 1, -1 for player 2, 0 for no one, -2 for draw

    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ": return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
        
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ": return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ": return board[0][2]
    
    return -2 if check_draw(board) else 0

def get_pos(pos):
    try:
        val = int(input(f"Enter {pos}: "))
    except ValueError:
        print(f"Invalid {pos}")
        return get_pos(pos)
    if val < 0 or val > 2:
        print(f"Invalid {pos}")
        return get_pos(pos)
    return val

pmap = lambda x: "X" if x == -1 else "O" if x == 1 else " "
def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(map(pmap, row)))
        print("-" * 11)  # This will add a separator line between rows

curr_player = 1
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while check_win(board) in [0, -2]:
    print_board(board)
    print(f"Player {1 if curr_player == 1 else 2}'s turn ({pmap(curr_player)})")
    row, col = get_pos("row"), get_pos("col")

    if board[row][col] != " ":
        print("Invalid move")
        continue

    board[row][col] = curr_player
    curr_player = -curr_player

print_board(board)
if check_win(board) == 1:
    print("Player 1 wins!")
elif check_win(board) == -1:
    print("Player 2 wins!")
else:
    print("It's a draw!")