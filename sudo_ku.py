#!/usr/bin/python
#~ bguillem // simple backtracking sudoku solver

import sys


def check_if_no_duplicates(line):
    dup = "0123456789"
    duplicates = list(dup)
    ind_in_duplicate = 0
    index = 0

    while (index < len(line)):
        if (line[index] >= '0' and line[index] <= '9'):
            ind_in_duplicate = int(line[index])
            if (duplicates[ind_in_duplicate] == "x" and ind_in_duplicate != 0):
                return False
            else:
                duplicates[ind_in_duplicate] = "x"
        index += 1
    return True



def check_if_line_is_valid(line):
    result = []

    if (len(line) != 10):
        print("Error: line should be 10 characters long, including the newline character.", file=sys.stderr)
        sys.exit(-1)
    for index in range (len(line)):
        if (line[index] < '0' or line[index] > '9') and line[index] != '\n':
            print("Error: character %c is not valid !", line[index])
            sys.exit(-1)
    if (check_if_no_duplicates(line) == False):
        print("Duplicates numbers spotted on this line :", file=sys.stderr)
        print(line, file=sys.stderr)
        sys.exit(-1)

    for i in range(9):
        result.append(int(line[i]))
    return result



def display_usage(return_value):

    print("sudo_ku\n\tpython sudo_ku [map]", file=sys.stderr)
    print("map sould be file containing a 9 by 9 square, with 0 in empty spots, as such :", file=sys.stderr)
    print("\t013500000", file=sys.stderr)
    print("\nTo display this message, please use the \"help\" flag.", file=sys.stderr)
    sys.exit(return_value)



def error_handling(nb_args, args):
    file_d = 0
    result = []

    if (nb_args != 2):
        display_usage(-1)
    elif (args[1] == "help"):
        display_usage(0)

    try:
        file_d = open(args[1], "r")
    except IOError:
        print("Error: file could not be opened.\nPlease check \"help\" flag for more info.", file=sys.stderr)
        sys.exit(-1)
    for line in file_d:
        result.append(check_if_line_is_valid(line))
    return result



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



board = error_handling(len(sys.argv), sys.argv)
print("Successfully loaded map :")
for i in range(0, len(board)):
    print(board[i])

print("\nstarting solver\n. . .")
solve_sudoku(board)
print("done.")
for i in range(0, len(board)):
    print(str(board[i]))
