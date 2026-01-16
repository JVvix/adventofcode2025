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
rows = []

for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        areas.append(area(coordinates[i], coordinates[j]))

areas.sort()
# print(areas[len(areas)-1])

# part 2
# 2026-01-15
# 15:48 to 17:04

import shapely as sl

for i in range(len(coordinates)):
    coordinates[i] = [int(coord) for coord in coordinates[i]]

def create_box(c1, c2):
    polygon = sl.Polygon([[c1[0], c2[1]], [c2[0], c2[1]], [c2[0], c1[1]], [c1[0], c1[1]]])
    return polygon
    # return sl.box(min(c1[0], c2[0]), min(c1[1], c2[1]), max(c1[0], c2[0]), max(c1[1], c2[1]))

poly = sl.Polygon(coordinates)

largest = 0

for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        box = create_box(coordinates[i], coordinates[j])
        if sl.within(box, poly):
            if area(coordinates[i], coordinates[j]) > largest:
                largest = area(coordinates[i], coordinates[j])

print(largest)
