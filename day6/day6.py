#!/usr/bin/env/ python
# Faye Ly
# advent of code 2025
# 2026-01-08
# part 1
# 16:23 to 16:54

total = 0

rows = []

columns = []

with open("input6.txt", "r") as file:
    for line in file:
        rows.append(line.strip("\n").split())
        # print(rows)

for i in range(len(rows[0])): #  colummns
    # print(i)
    per_column = []
    for j in range(len(rows)): # rows
        print(j)
        per_column.append(rows[j][i]) 
    columns.append(per_column)

# print(len(rows))
print(columns)

for column in columns:
    total += eval(column[4].join(column[:4]))

print(total)
