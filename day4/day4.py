#!/usr/bin/env python
# Faye Ly
# advent of code 2025
# https://adventofcode.com/2025/day/4
# 2026-01-05
#
def matrix_checker(list_one, list_two):
    if len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] != list_two[i]:
                # print(list_one[i])
                # print(list_two[i])
                return False
        return True
    else:
        return False

board = []


movable_rolls = 0
count = 0
adjacent_rolls = 0
lines = 0

with open("input4.txt", "r") as file:
    for line in file:
        lines += 1
        line = list(line.strip("\n"))
        line.insert(0, ".")
        line.append(".")
        # line = [True if item == "@" else False for item in line]
        board.append(line)

# print(len(board[0]))

# board = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n @.@.@@@.@.".split("\n")
# print(board)


# board = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.".split("\n")
# for i in range(len(board)):
#     board[i] = list(board[i])
#     board[i].insert(0, ".")
#     board[i].append(".")
    # board[i] = [True if item == "@" else False for item in board[i]]

filler = [] 
for i in range(len(board[0])):
    filler.append(".")


# print(board)
    
board.insert(0, filler)
board.append(filler)

# print(board)
new_board = []

previous_movable = 0

# while not matrix_checker(board, new_board):
# while previous_movable != movable_rolls:
while count < 10000:
    previous_movable = movable_rolls
    new_board.append(filler)
    for i in range(1,len(board)-1): # row
        new_row = ["."]
        for j in range(1,len(board[i])-1): # colum
            adjacent_rolls = 0 
            if board[i][j] == "@":
                # check left and right
                if board[i][j-1] == "@":
                    adjacent_rolls += 1
                if board[i][j+1] == "@":
                    adjacent_rolls += 1

                # check left and right (up)
                if board[i-1][j-1] == "@":
                    adjacent_rolls += 1
                if board[i-1][j+1] == "@":
                    adjacent_rolls += 1
                if board[i-1][j] == "@":
                    adjacent_rolls += 1
                
                # check left and right (down)
                # print(j+1)
                #
                
                if board[i+1][j-1] == "@":
                    adjacent_rolls += 1
                if board[i+1][j+1] == "@":
                    adjacent_rolls += 1
                if board[i+1][j] == "@":
                    adjacent_rolls += 1

                if adjacent_rolls < 4:
                    # new_board[i][j] = "x"
                    new_row.append("x")
                    movable_rolls += 1
                else:
                    new_row.append(board[i][j])
            elif board[i][j] == "x":
                new_row.append(".")
            else:
                new_row.append(board[i][j])
        new_row.append(".")
        new_board.append(new_row)
    new_board.append(filler)

    print("")
    for i in range(1, len(new_board)-1):
        print("".join(new_board[i]))
    print("movable_rolls:" + str(movable_rolls))
    # if matrix_checker(board, new_board) == True:
    #     break

    board = new_board
    new_board = []

    if movable_rolls == previous_movable:
        break

        # print("current row: " + str(i))
        # print("current rolls: " + str(movable_rolls))

print("")

# for i in range(1, len(board)-1):
#     print("".join(new_board[i]))

# print(board[10][9])

print(movable_rolls)

