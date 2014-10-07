#!/bin/python
import sys
from termcolor import colored, cprint
from random import randint

board = []

#Below is the length and width of the board array
for x in range(10):
    board.append(["O"] * 10)
def print_board(board):
    for row in board:
        print " ".join(row)

cprint ("Let's play Battleship!", "red")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#Remove below once testing is done
print "SURVEY SAYS!"
cprint ("Ship is at row: " + str(ship_row), "cyan")
cprint ("Ship is at col: " + str(ship_col), "cyan")

turn = -1
for guess in range(11):
    turn += 1
    turnsLeft = 10 - turn
    guess_row = int(raw_input("Please Guess A Row    : "))
    guess_col = int(raw_input("Please Guess A Column : "))

    if guess_row == ship_row and guess_col == ship_col:
        cprint ("Congratulations! You sunk my battleship!", "red", attrs=["bold"])
        break
    else:
        if (guess_row < 0 or guess_row > len(board)) or (guess_col < 0 or guess_col > len(board)):
            print "Oops, that's not even in the ocean."
            print "Please guess within 0 and " + len(board)
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Your round went into the ocean!"
            board[guess_row][guess_col] = "X"
            print "Turn", turn + 1 
            #Trying to get a "Turn X of Y"
            #print "Turn " + turn + "of " + turnsleft
            #turn += 1

            print_board(board)
            
            if turn == 9: #Remember 0 counts!
                print "Game Over"
                break
