#!/usr/bin/env python

'''
Python Battleship game.

Learning objectives:
Place multiple ships of multiple lengths, distributed randomly.
How to score hits?
Implement game stats - Print / read to a flat file (json), then use a database
Make it a multi-player game
Score for each player, different board and ships? Websockets to play from a different computer? Login? Sure.
Multiple types of ships ^ * #...

Bugs:
Ships float over one another
How to determine if a ship is sunk? Store coordinates for each ship?
I think Ship needs to be a class.
Maybe Game needs to be a class to track ships, players, etc.
'''

from random import randint
import sys

'''
Set global variables
'''
game_over = False
guess_col = 0
guess_row = 0

'''
Define functions
'''
def print_board(board):
    print "\n"
    for row in board:
        print " ", " ".join(row)
    print "\n"

'''
Build the board
'''
board = []
for i in range(1,6):
    row = []
    for i in range(1,6):
        row.append("O")
    board.append(row)

'''
Build and place the ships
'''
print "how many ships would you like?"
while True:
    num_ships = int(raw_input("Enter an integer between 1 and 3: "))
    if num_ships not in range(1,4):
        print "That's not valid."
    else:
        break

ship_types = ["^", "*", "#"]
ships = []

for i in range(num_ships):
    '''
    Try 3 times to place each ship to avoid collisions
    A ship will be 3 units long
    Bug fix: place the ship's coordinates in a list, that way we remember where each ship lives,
    and if placing a ship fails, retry twice before throwing away the list
    '''
    print "Ship", i
    ship_type = ship_types.pop()

    print "Attempting to place ship..."
    ship_row = randint(0,4)
    ship_col = randint(0,4)
    ship = []
    ship_bow = []
    ship_mid = []
    ship_stern = []

    if board[ship_row][ship_col] == "O":
        board[ship_row][ship_col] = ship_type
    else:
        pass

    ''' Ship will be aligned on either x or y axis'''
    alignment = randint(1,2)
    # 1 means north-south
    # 2 means east-west

    if alignment == 1:
        # ships are three units long
        for j in range(3):
            '''check for edge of board'''
            if ship_row + j > 4:
                print "row is", ship_row + 1
                print "You're off the board"
                for k in range(2):
                    if (board[ship_row - k][ship_col] == ship_type):
                        pass
                    else:
                        board[ship_row - k][ship_col] = ship_type
            else:
                board[ship_row + j][ship_col] = ship_type
    else:
        # ships are three units long
        for j in range(3):
            if ship_col + j > 4:
                print "col is", ship_col + 1
                print "You're off the board"
                for k in range(2):
                    if (board[ship_row][ship_col - k] == ship_type):
                        pass
                    else:
                        board[ship_row][ship_col - k] = ship_type
            else:
                board[ship_row][ship_col + j] = ship_type

print "Here are your ships:"
print ship_row, " ", ship_col



'''
Start the game
'''
print "\n"
print "Welcome to Battleship!"

while not game_over:
    print_board(board)

    print "Enter the coordinates you want to fire upon:"
    guess_col = int(raw_input("Enter an integer from 1 to 5 to specify the column: "))
    while guess_col not in range(1,6):
        print "That's not a valid number."


    guess_row = int(raw_input("Enter an integer from 1 to 5 to specify the row: "))
    while guess_row not in range(1,6):
        print "That's not a valid number."

    '''
    Programmers count from 0
    '''
    guess_col -= 1
    guess_row -= 1



    if board[guess_row][guess_col] != "O":
        board[guess_row][guess_col] = "X"
        print_board(board)
        print " You win!", "\n"
        game_over = True
    else:
        board[guess_row][guess_col] = "X"
        print_board(board)
