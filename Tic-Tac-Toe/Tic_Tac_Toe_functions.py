def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print()
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        if i < 2:
            print("-------------")
    print()

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, row, col, player):
    board[row][col] = player

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def switch_player(player):
    return 'O' if player == 'X' else 'X'
