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
        # print(line)
        rows.append(line.strip("\n").split())
        # print(rows)

for i in range(len(rows[0])): #  colummns
    # print(i)
    per_column = []
    for j in range(len(rows)): # rows
        # print(j)
        per_column.append(rows[j][i]) 
    columns.append(per_column)

# print(len(rows))
# print(rows)

for column in columns:
    # print(eval(column[len(column)-1].join(column[:len(column)-1])))
    total += eval(column[len(column)-1].join(column[:len(column)-1]))

# print(total)

# 2026-01-09
# 2026-01-10
# part 2
# 15:50 to 18:28
# 06:30 to 07:34
# partial solution taken from HyperNeutrino

# HyperNeutrino 

grid = [line.strip("\n") for line in open("input6.txt")]

value_rows = []
values = []

columns = list(zip(*grid))
for column in columns:
    # print(len(column))
    number = ""
    if not all(s == '' or s.isspace() for s in column):
        print(column)
        for i in range(len(column)-1):
            if column[i] != '':
                number += column[i]
    values.append(number)


# print(values)

operators = []
new_values = []
value_sublist = []

for number in values:
    if number == '':
        new_values.append(value_sublist)
        value_sublist = []
    else:
        value_sublist.append(number)
new_values.append(value_sublist)

print(new_values)

for column in columns:
    if column[len(column)-1] != " ":
        operators.append(column[len(column)-1])
    else:
        continue

total = 0

# print(len(new_values))
# print(operators)


for i in range(len(new_values)):
    print(operators[i].join(new_values[i]))
    total += eval(operators[i].join(new_values[i]))

print(total)
