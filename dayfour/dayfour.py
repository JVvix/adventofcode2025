

board = []


movable_rolls = 0
adjacent_rolls = 0
lines = 0

with open("input4.txt", "r") as file:
    for line in file:
        lines += 1
        line = list(line.strip("\n"))
        line.insert(0, ".")
        line.append(".")
        line = [True if item == "@" else False for item in line]
        board.append(line)

print(len(board[0]))

# board = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n @.@.@@@.@.".split("\n")
#
#
# for i in range(len(board)):
#     board[i] = list(board[i])
#     board[i].insert(0, ".")
#     board[i].append(".")
#     board[i] = [True if item == "@" else False for item in board[i]]

filler = [] 
for i in range(len(board[0])):
    filler.append(False)


# print(board)
    
board.insert(0, filler)
board.append(filler)

# print(board)

for i in range(1, len(board)): # row
    for j in range(1, len(board[i])): # colum
        adjacent_rolls = 0 
        if board[i][j]:
            # check left and right
            if board[i][j+1]:
                adjacent_rolls += 1
            if board[i][j-1]:
                adjacent_rolls += 1

            # check left and right (up)
            if board[i-1][j+1]:
                adjacent_rolls += 1
            if board[i-1][j]:
                adjacent_rolls += 1
            if board[i-1][j-1]:
                adjacent_rolls += 1
            
            # check left and right (down)
            # print(j+1)
            #
            
            if board[i+1][j+1]:
                adjacent_rolls += 1
            if board[i+1][j]:
                adjacent_rolls += 1
            if board[i+1][j-1]:
                adjacent_rolls += 1

            if adjacent_rolls < 4:
                movable_rolls += 1

        # print("current row: " + str(i))
        # print("current rolls: " + str(movable_rolls))

print(movable_rolls)
