from functions import *

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + " goes first!")
    game_status = input('Are you ready to play? Enter Yes or No.')
    if game_status.lower()[0] == 'y':
        game = True
    else:
        game = False
    while game:
        if turn == 'Player 1':
            display_board(board)
            print('Player 1 Turn, \n ')
            position = player_choice(board)
            while position == -1:
                print("Uh Oh! that space is filled try again! \n")
                position = player_choice(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print('Congratulations! Player 1 wins the game!')
                game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('It is a tie!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            print('Player 2 Turn, \n')
            position = player_choice(board)
            while position == -1:
                print("Uh Oh! that space is filled try again! \n")
                position = player_choice(board)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print('Congratulations! Player 2 wins!')
                game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('It is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
