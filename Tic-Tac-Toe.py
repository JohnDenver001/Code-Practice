from Tic_Tac_Toe_functions import *

board = create_board()
current_player = 'X'
while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")

    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
    except ValueError:
        print("Please enter numbers between 0 and 2.")
        continue

    if not is_valid_move(board, row, col):
        print("Invalid move.")
        continue

    make_move(board, row, col, current_player)

    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break

    if check_draw(board):
        print_board(board)
        print("It's a draw WHAT A GAME HAHA!")
        break

    current_player = switch_player(current_player)
