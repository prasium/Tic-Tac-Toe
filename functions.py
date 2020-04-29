#for player's input
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Enter Player 1 Marker Choice (X or O) : ').upper()
    if marker=='X':
        p1=marker
        p2='O'
    else :
        p1=marker
        p2='X'
    return (p1,p2)

#for displaying the board
def display_board(board):
    print('\n'*50)
    for i in range (9,1,-3):
        print(board[i-2] + "|" + board [i-1] + "|" + board [i])
        print("-----")


#defining a place marker
def place_marker(board, marker, position):
    board[position]=marker

#checks win
def win_check(board, mark):
   return ((board[1]==board[2]==board[3]==mark)or   #lower row
           (board[4]==board[5]==board[6]==mark)or   #middle row
           (board[7] == board[8] == board[9] == mark) or # upper row
           (board[1] == board[4] == board[7] == mark) or #left column
           (board[2] == board[5] == board[8] == mark) or #mid column
           (board[3] == board[6] == board[9] == mark) or #right column
           (board[1] == board[5] == board[9] == mark) or #other diagonal
           (board[3] == board[5] == board[7] == mark))   #main diagonal

# decides which player starts first
import random
def choose_first():
    choice=random.randint(1,2)
    if choice==1:
        return 'Player 1'
    else:
        return 'Player 2'
#checks the space on board of entered mark
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
#checks full board
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
#asks the user for position to enter
def player_choice(board):
    position=int(input('Enter Position (1-9) to fill on the board : '))
    if space_check(board,position):
        return position
    else :
        return -1
#asks to play again?
def replay():
    ask=input("Would you like to play again?(Y/N) : ")
    if ask.lower()[0]=='y':
        return True
    else :
        return False