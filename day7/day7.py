#!/usr/bin/env python

# Faye Ly
# Advent of Code 2025
# Day 7
# 2026-01-10

# part 1
# 09:13 to 09:45

# grid = [list(line.strip("\n")) for line in open("input.txt")]

splits = 0
grid = [list(line.strip("\n")) for line in open("input.txt")]

# grid = []
#
# for row in old_grid:
#     if row != ["."] * len(row):
#         grid.append(row)

for row in range(len(grid)):
    for character in range(len(grid[row])):
        if grid[row][character] == "S" or grid[row][character] == "|":
            if grid[row+1][character] == "^":
                grid[row+1][character-1] = "|"
                grid[row+1][character+1] = "|"
                splits += 1
            else:
                if row < len(grid[row])-1:
                    grid[row+1][character] = "|"

    # print("".join(grid[row-1]))
    # print("".join(grid[row]))
    # print("new splits: " + str(splits - old_splits))
    # print()

    if row == len(grid)-1:
        for character in range(len(grid[row])):
            if grid[row-1][character] == "|":
                grid[row][character] ="|"

        # print(character)

for row in grid:
    print("".join(row))

# print(str(splits) + " splits")

# part 2
# 2026-01-10 to 2026-01-12

splits = 0

# grid = [list(line.strip("\n")) for line in open("example.txt")]
# j ways to hit A + k ways to hit B...
# recursion?

total_paths = []
paths = []


for i in range(len(grid)):
# for i in range(8):
    paths = [0] * len(grid[i])
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            paths[j] += 1
        if grid[i][j] == "|":
            paths[j] += total_paths[j]
        if grid[i][j] == "^":
            paths[j-1] += total_paths[j]
            paths[j+1] += total_paths[j]
    # print("".join(grid[i]))
    # print("".join(str(item) for item in paths))
    total_paths = paths

print(sum(total_paths))
#
#
