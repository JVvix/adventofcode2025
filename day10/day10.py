#!/usr/bin/env python

# Faye Ly
# advent of code 2025
# Day 10
# 2026-01-16

# part 1
#
# 01/16/2026
# 16:29 to 17:31
#
# 01/17/2026
# 08:52 to 09:25
# 10:55 to 11:47
# 18:09 to 18:37

def toggle(lights, buttons, order):
    count = 0

    actual_buttons = ["."] * len(lights)

    for i in range(len(order)):
        if order[i] == "1":
            count += 1
            for j in range(len(buttons[i])):
                if actual_buttons[int(buttons[i][j])] == ".":
                    actual_buttons[int(buttons[i][j])] = "#"
                else:
                    actual_buttons[int(buttons[i][j])] = "."
        

    # print(lights)
    if actual_buttons == lights:
        # print(actual_buttons)
        return count
        # print(count)

def solve(parts):
    lights = list(parts[0][1:-1])
    voltage = parts[len(parts)-1].split(",")
    voltage[0] = voltage[0][1:]
    voltage[-1] = voltage[-1][:len(voltage[-1])-1]

    order = []
    buttons = []

    for i in range(1, len(parts)-1):
        order.append("1")

        switch = parts[i].split(",")
        switch[0] = switch[0][1:]
        switch[-1] = switch[-1][:-1]

        buttons.append(switch)

    # print(toggle(lights, buttons, order))

    order = "".join(order)
    # print(int(order, 2))
    variations = []
    # print(2 ** len(buttons))
    for i in range(2 ** len(buttons)):
        # print(bin(i)[2:].zfill(len(order)))
        variations.append(bin(i)[2:].zfill(len(order)))

    least_buttons = 19204122414
    
    for variation in variations:
        if toggle(lights, buttons, variation) != None and toggle(lights, buttons, variation) < least_buttons:
            least_buttons = toggle(lights, buttons, variation)
    return least_buttons

instructions = [line.strip("\n") for line in open("example.txt")]
instructions = [line.strip("\n") for line in open("input.txt")]

total = 0

for i in range(len(instructions)):
# for i in range(1):
    parts = instructions[i].split()
    total += solve(parts)

print(total)

# part 2
# 01/18/2026
