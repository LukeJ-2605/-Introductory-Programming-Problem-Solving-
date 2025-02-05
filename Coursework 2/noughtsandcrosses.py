
#Student Name: Luke Johnson
#Student Number: 2222880
import random
import os.path
import json
random.seed()

'''This function draws the board using print functions and the board from the
play game python file.'''
def draw_board(board):
    print(' ----------- ')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
    print(' ----------- ')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
    print(' ----------- ')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
    print(' ----------- ')
    pass

'''This function prints the welcome function along with the board from the draw board function.'''
def welcome(board):
    print('Welcome to the "Unbeatable Naughts and Crosses" game.\nThe board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')
    pass

'''This function resets the board so that all 'cells' are empty.'''
def initialise_board(board):
    board = [ [' ',' ',' '],\
              [' ',' ',' '],\
              [' ',' ',' ']]
    return board

'''This function asks the player for the cell number that they would like to place an 'X' in.
it then checks to see if the input is valid and if the cell is empty, before placing the 'X'
in the empty cell.'''
def get_player_move(board):
    while True:
        p_move = input('Choose your square: ')
        if p_move.isdigit():
            p_move = int(p_move)
            if p_move >=1 and p_move <=9:
                p_moveint = int(p_move) - 1
                row = p_moveint // 3
                col = p_moveint % 3
                if board[row][col] == ' ':
                    break
        print('Invalid Input')
    return row, col

'''This function chooses the computers move. It is programmed to prioriitise winning. This
means that if it sees a way to win, it will prioritise that move over blocking the opponent.
I did this by using a bunch of if and elif statements to code each possible winning move for
both the 'X' player and the 'O' player. It also is coded to select a specific cell based on
where the players places their first 'X'. '''
def choose_computer_move(board):
    #1ST row for o
    if board[0][0] == 'O' and board[0][2] == 'O' and board[0][1] == ' ':
        row = 0
        col = 1
        
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == ' ':
        row = 0

        col = 2
        
    elif board[0][1] == 'O' and board[0][2] == 'O' and board[0][0] == ' ':
        row = 0
        col = 0
        
    #2ND row for o
    elif board[1][0] == 'O' and board[1][2] == 'O' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == ' ':
        row = 1
        col = 2
        return row, col
    elif board[1][1] == 'O' and board[1][2] == 'O' and board[1][0] == ' ':
        row = 1
        col = 0
        
    #3RD row for o
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[2][0] == 'O' and board[2][2] == 'O' and board[2][1] == ' ':
        row = 2
        col = 1
           
    elif board[2][1] == 'O' and board[2][2] == 'O' and board[2][0] == ' ':
        row = 2
        col = 0
        
    #1ST column for o
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == ' ':
        row = 2
        col = 0
        
    elif board[0][0] == 'O' and board[2][0] == 'O' and board[1][0] == ' ':
        row = 1
        col = 0
        
    elif board[1][0] == 'O' and board[2][0] == 'X' and board[0][0] == ' ':
        row = 0
        col = 0
        
    #2ND column for o
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == ' ':
        row = 2
        col = 1
        
    elif board[0][1] == 'O' and board[2][1] == 'O' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[1][1] == 'O' and board[2][1] == 'O' and board[0][1] == ' ':
        row = 0
        col = 1
        
    #3RD column for o
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[0][2] == 'X' and board[2][2] == 'O' and board[1][2] == ' ':
        row = 1
        col = 2
        
    elif board[1][2] == 'O' and board[2][2] == 'O' and board[0][2] == ' ':
        row = 0
        col = 2
        
    #Diagonals for o
    elif board[0][0] == 'O' and board[2][2] == 'O' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[1][1] == 'O' and board[2][2] == 'O' and board[0][0] == ' ':
        row = 0
        col = 0
        
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
        row = 2
        col = 0
        
    elif board[0][2] == 'O' and board[2][0] == 'O' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == ' ':
        row = 0
        col = 2
    
    #1ST row for x
    elif board[0][0] == 'X' and board[0][2] == 'X' and board[0][1] == ' ':
        row = 0
        col = 1
        
    elif board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == ' ':
        row = 0
        col = 2
        
    elif board[0][1] == 'X' and board[0][2] == 'X' and board[0][0] == ' ':
        row = 0
        col = 0
        
    #2ND row for x
    elif board[1][0] == 'X' and board[1][2] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == ' ':
        row = 1
        col = 2
        return row, col
    elif board[1][1] == 'X' and board[1][2] == 'X' and board[1][0] == ' ':
        row = 1
        col = 0
        
    #3RD row for x
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[2][0] == 'X' and board[2][2] == 'X' and board[2][1] == ' ':
        row = 2
        col = 1
        
    elif board[2][1] == 'X' and board[2][2] == 'X' and board[2][0] == ' ':
        row = 2
        col = 0
        
    #1ST column for x
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == ' ':
        row = 2
        col = 0
        
    elif board[0][0] == 'X' and board[2][0] == 'X' and board[1][0] == ' ':
        row = 1
        col = 0
        
    elif board[1][0] == 'X' and board[2][0] == 'X' and board[0][0] == ' ':
        row = 0
        col = 0
        
    #2ND column for x
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == ' ':
        row = 2
        col = 1
        
    elif board[0][1] == 'X' and board[2][1] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[1][1] == 'X' and board[2][1] == 'X' and board[0][1] == ' ':
        row = 0
        col = 1
        
    #3RD column for x
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[0][2] == 'X' and board[2][2] == 'X' and board[1][2] == ' ':
        row = 1
        col = 2
        
    elif board[1][2] == 'X' and board[2][2] == 'X' and board[0][2] == ' ':
        row = 0
        col = 2
    elif board[2][2] == 'X' and board [0][2] == 'X' and board[1][2] == ' ':
        row = 1
        col = 2
        
    #Diagonals for x
    elif board[0][0] == 'X' and board[2][2] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[1][1] == 'X' and board[2][2] == 'X' and board[0][0] == ' ':
        row = 0
        col = 0
        
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
        row = 2
        col = 0
        
    elif board[0][2] == 'X' and board[2][0] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == ' ':
        row = 0
        col = 2

    #Individuals
    elif board[0][0] == 'X' and board[0][2] == ' ':
        row = 0
        col = 2
        
    elif board[0][0] == 'X' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[0][0] == 'X' and board[2][0] == ' ':
        row = 0
        col =  2
        
    elif board[0][0] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[0][2] == 'X' and board[2][0] == ' ':
        row = 2
        col = 0
        
    elif board[0][2] == 'X' and board[2][2] == ' ':
        row = 2
        col = 2
        
    elif board[0][2] == 'X' and board[1][1] == 'X':
        row = 1
        col = 1
        
    elif board[0][1] == 'X' and board[2][1] == ' ':
        row = 2
        col = 1
        
    elif board[1][0] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1
        
    elif board[1][1] == 'X' and board [0][2] == ' ':
        row = 0
        col = 2

    elif board[0][2] == 'X' and board[1][1] == ' ':
        row = 1
        col = 1

    elif board[2][0] == 'X' and board[1][0] == ' ':
        row = 1
        col = 0

    else:
        for row in range(0,3):
            for col in range(0,3):
                if board[row][col] == ' ':
                     return row, col
    return row, col

'''This function checks if either the player or computer has won. It does this by checking each
individual row, column and diagonal to see if there is any two marks the same in a line. '''
def check_for_win(board, mark):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    #Column Wins
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    #Diagonal Wins
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    else:
        return False
    return False

'''This function checks for a draw. It does this by checking to see if there is any empty cells.
if there are empty cells, then there isn't a draw. If all cells are full, the game is over and
both players have tied. '''
def check_for_draw(board):
    if board[0][0] == ' ' or board[0][1] == ' ' or board[0][2] == ' '\
       or board[1][0] == ' ' or board[1][1] == ' ' or board[1][2] == ' '\
       or board[2][0] == ' ' or board[2][1] == ' ' or board[2][2] == ' ':
        return False
    return True

'''This function essentially runs the game. It calls upon  the functions for player move,
computer move, check for win and check for draw. It returns 1 if the player wins, 0 if they
draw and -1 if they lose. This is then added to the score.'''
def play_game(board):
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        print('Your Move: ')
        draw_board(board)
        check_for_draw(board)
        if check_for_draw(board) == True:
            print("It's a draw!")
            return 0
        check_for_win(board,'X')
        if check_for_win(board,'X') == True:
            print('You Win!')
            return 1
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        print("The computer's move: ")
        draw_board(board)
        check_for_draw(board)
        if check_for_draw(board) == True:
            print("It's a draw!")
            return 0
        check_for_win(board, 'O')
        if check_for_win(board, 'O') == True:
            print('You Lose!')
            return -1
    return 0

'''This function displays the menu for users to select to either play the game,
save their score, view the leaderboard, or quit the game. It is displayed after
each win, loss or draw. '''
def menu():
    print('Enter one of the following options:')
    print('        1 - Play the game')
    print('        2 - Save your score in the leaderboard')
    print('        3 - Load and display the leaderboard')
    print('        q - End the program')
    choice = input('1, 2, 3 or q? ')
    return choice

'''This function checks to see if there is a file called 'leaderboard.txt'.
if there is, it will load that file and return the data ffrom the file
as a dictionary. If there isn't a file it will create one and then load
the data as a disctionary.'''
def load_scores():
    while True:
        if os.path.exists('leaderboard.txt') == True:
            leaders = json.load(open('leaderboard.txt'))
            break
        else:
            leaders = {}
            json_leaders = json.dumps(leaders)
            file = open('leaderboard.txt','w')
            file.write(json_leaders)
            file.close()
    return leaders

'''This function saves the users score to the text file as a dictionary. First
it loads the current scores using the load scores function, and then asks the
user for their name to add to the leaderboard. '''
def save_score(score):
    leaders = load_scores()
    name = input('What is your name? ')
    new_leaders = {name:score}
    leaders.update(new_leaders)
    with open('leaderboard.txt', 'w') as file:
        file.write(json.dumps(leaders))
    file.close()
    return 

'''This function prints the leaderboard from the created dictionary 'leaders'
It prints a layout with titles NAME and SCORE and then searches through
the dictionary for the names (the key) and the score (th value) and displays
them for the user to see.'''
def display_leaderboard(leaders):
    print('Here is the leaderboard:')
    print('----------------')
    print(' NAME  ¦  SCORE ')
    print('----------------')
    for key, val in leaders.items():
        print(key, '  :   ', val)
    print('----------------')
    pass

