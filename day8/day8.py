#!/usr/bin/env python
# Faye Ly
# advent of code 2025
# day 8
# 2026-01-12

# part 1
# 18:38 to 18:38

import math
from collections import Counter

def straight_line(coords_1, coords_2):
    a = int(coords_1[0]) - int(coords_2[0])
    b = int(coords_1[1]) - int(coords_2[1])
    c = int(coords_1[2]) - int(coords_2[2])
    a = a * a
    b = b * b
    c = c * c
    return math.sqrt(a + b + c)

coordinates = [line.strip("\n").split(",") for line in open("input.txt")]
distances = []
groups = []

for i in range(len(coordinates)):
    groups.append(i)
    for j in range(i+1, len(coordinates)):
        distances.append([straight_line(coordinates[i], coordinates[j]), i, j])

distances.sort()

distances = distances[:1000]
# distances = distances[:10]
print(len(distances))

for i in range(len(distances)):
    start = groups[distances[i][1]]
    end = groups[distances[i][2]]
    for j in range(len(groups)):
        if groups[j] == end:
            groups[j] = start
            # groups[j] = groups[distances[i][2]]
        

# print(distances)
print(groups)
print(set(groups))

group_types = set(groups)

group_counts = []
# group_counts = Counter(groups)

for item in group_types:
    group_counts.append(groups.count(item))

group_counts.sort()

print(group_counts)

product = 1

for i in range(len(group_counts)-3, len(group_counts)):
    print(group_counts[i])
    product = product * group_counts[i]

print(product)
