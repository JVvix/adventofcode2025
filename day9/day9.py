#!/usr/bin/env python
# Faye Ly
# advent of code 2025
# day 9
# 2026-01-14

# part 1
# 15:42 to 16:04

def area(c1, c2):
    x_distance = abs(int(c1[0]) - int(c2[0]))
    y_distance = abs(int(c1[1]) - int(c2[1]))
    x_distance += 1
    y_distance += 1
    return x_distance * y_distance

coordinates = [line.strip("\n").split(",") for line in open("input.txt")]
areas = []

for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        areas.append(area(coordinates[i], coordinates[j]))

areas.sort()
print(areas[len(areas)-1])
