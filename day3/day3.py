#!/usr/bin/env python
# Faye Ly 2026-01-05
# Advent of Code 2025
# https://adventofcode.com/2025/day/3
# find highest p in range(1,) ssible value in arranged order 

def highest_value(number):
    first_digit = 0
    second_digit = 0
    
    number = number.strip("\n")

    first_digit = max(number)
    if number.count(first_digit) > 1:
        return int(first_digit) * 11
    else:
        index = number.find(first_digit)
        if index < len(number)-1:
            for i in range(index+1, len(number)):
                if second_digit < int(number[i]):
                    second_digit = int(number[i])
            return int(first_digit) * 10 + second_digit
        else: 
            second_digit = first_digit
            first_digit = max(number[:len(number)-1])
            index = number.find(first_digit)
            return int(first_digit) * 10 + int(second_digit)

def highest_value_two(number):
    # find greatest digit for 12 numbers
    # if number < next number..  go to next number.
    biggest_digits = []
    number = number.strip("\n")
    digits = list(number)
    biggest_digit = "0"
    index = -1
    remaining_digits = 11

    while remaining_digits > -1:
        # print("remaining_digits are " + str(remaining_digits))
        for i in range(index+1, len(digits)-remaining_digits):
            # print("current biggest digit: " + biggest_digit)
            # print("current digit: " + digits[i])
            if digits[i] > biggest_digit:
                biggest_digit = digits[i]
                index = i
        biggest_digits.append(biggest_digit)
        remaining_digits -= 1
        biggest_digit = "0"


    # for i in range(indexes[0],len(digits)-1):
    #     # check if next number is less than current number. if so store current number. 
    #     # this gets us the bigger numbers for 1, 3 and 4, but how do we get the fillups?
    #     if digits[i] < digits[i+1] and i+1 not in indexes:
    #         biggest_digits.append(digits[i+1])
    #         indexes.append(i+1)
    #     else:
    #         if i not in indexes:
    #             biggest_digits.append(digits[i])
    #             indexes.append(i)

    # failsafe
    


    print("".join(biggest_digits))
    return "".join(biggest_digits)
    # 12 digits!!! highest 12 digits.

test_set = ["987654321111111\n","811111111111119\n","234234234234278\n","818181911112111\n"]

total = 0

with open("input3.txt", "r") as file:
    for line in file:
        total += int(highest_value_two(line))

# for battery in test_set:
#     # print(highest_value(str(battery)))
#     # print(highest_value(str(battery)))
#     highest_value_two(str(battery))
#     total += int(highest_value_two(str(battery)))

print(total)
