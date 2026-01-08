#!/usr/bin/env python
# Faye Ly
# advent of code 2025
# https://adventofcode.com/2025/day/5
# 2026-01-06

no_overlaps = []
ranges = []
ids = []
fresh_ids = []
total_fresh_ids = 0
temp_list = []
max_value = 0

with open("input5.txt", "r") as file:
    for line in file:
        if "-" in line:
            ranges.append(line.strip("\n"))
        else:
            if line != "\n":
                ids.append(line.strip("\n"))

for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    ranges[i] = [int(item) for item in ranges[i]]

ranges.sort()
print(ranges)

# list(set(ranges))

# print(ranges)

# part 1

# for id in ids:
#     # print(id)
#     for each_range in ranges:
#         if int(id) in range(int(each_range[0]), int(each_range[1])+1):
#             # print(id)
#             fresh_ids.append(id)
#             break

# print(len(fresh_ids))

# part 2

# merge ranges

no_overlaps.append(ranges[0])

print(no_overlaps)

# for i in range(1,len(ranges)):
for i in range(1, len(ranges)):
    if no_overlaps[len(no_overlaps)-1][1] < ranges[i][0]:
        no_overlaps.append(ranges[i])
    elif no_overlaps[len(no_overlaps)-1][0] > ranges[i][1]:
        print("geez")
        # print(no_overlaps)
    elif no_overlaps[len(no_overlaps)-1][1] < ranges[i][1]:
        no_overlaps[len(no_overlaps)-1][1] = ranges[i][1]
    print(ranges[i])

for per_range in no_overlaps:
    total_fresh_ids += per_range[1] - per_range[0] + 1


        

# for i in range(0,len(ranges)-1):
    # # if len(ranges)-1 < i:
    # #     break
    # print(total_fresh_ids)
    # if int(ranges[i+1][1]) > int(ranges[i][1]):
    #     # print(f"{ranges[i][0]} to {ranges[i+1][1]}")
    #     total_fresh_ids += ranges[i+1][1] - ranges[i][0] + 1
    #     print(f"range: {ranges[i][0]} to {ranges[i+1][1]}")
    #     max_value = ranges[i+1][1]
    #     temp_list += range(ranges[i][0],ranges[i][1])
    # else:
    #     print(ranges[i])
    #     total_fresh_ids += ranges[i][1] - ranges[i][0] + 1
    #     temp_list += range(ranges[i][0],ranges[i][1])
    #     # print(ranges[i])

# print(len(total_fresh_ids))
print(total_fresh_ids)
# print(no_overlaps)
