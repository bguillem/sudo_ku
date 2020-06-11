#!/usr/bin/python
#~ bogdzn

import sys

def read_map(filepath):
    lines = 0
    cols = 0
    matrix = [[0 for x in range(9)] for y in range(9)]

    try:
        file = open(filepath, 'r')
    except IOError:
        print("Error: file could not be openend.", file = sys.stderr)
        exit(-1)
    while lines != 9:
        cols = 0
        character = file.readline()
        for c in character:
            matrix[lines][cols] = int(c)
            cols += 1
            if cols == 9 :
                lines += 1
                break
    return matrix



def display_usage(return_value):

    print("sudo_ku\n\tpython sudo_ku [map]", file=sys.stderr)
    print("map sould be file containing a 9 by 9 square, with 0 in empty spots, as such :", file=sys.stderr)
    print("\t013500000", file=sys.stderr)
    print("\nTo display this message, please use the \"help\" flag.", file=sys.stderr)
    sys.exit(return_value)



def print_board(board):

    if not board:
        print("No solution found.")
        exit(1)

    for i in range(len(board)):
        if i % 3 == 0 and i != 0 :
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])) :
            if j % 3 == 0 and j != 0 :
                print(" | ", end="")

            if j == 8 :
                print(board[i][j])
            else :
                print(str(board[i][j]) + " ", end="")



def find_first_empty_spot(board):

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return row, column
    return None



def is_valid_play(board, number, position):
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range (0, len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    for i in range(0, len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range (box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True



def solve_sudoku(board):
    empty_spot = find_first_empty_spot(board)

    if not empty_spot:
        return True
    else:
        row, column = empty_spot
    for i in range(1, 10):
        if is_valid_play(board, i, (row, column)):
            board[row][column] = i
            if solve_sudoku(board):
                return True
            board[row][column] = 0
    return False



#################################################
################# MAIN SCRIPT ###################
#################################################

if len(sys.argv) == 2 :
    if sys.argv[1] == "-help" :
        display_usage(0)

    sudoku = read_map(sys.argv[1])
    print_board(solve_sudoku(sudoku))
    exit(0)
display_usage(-1)

