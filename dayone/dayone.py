directions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
current_dial = 50
direction = None
turns = None
zeros = 0


def turn(input):
    global zeros, current_dial
    direction = input[0]
    turns = int(input[1:])

    # turns = turns % 100

    if direction == "L":
        for i in range(turns):
            current_dial -= 1

            if current_dial < 0:
                current_dial = 100 + current_dial

            if current_dial == 0:
                zeros += 1
    else:
        for i in range(turns):
            current_dial += 1
            if current_dial > 99:
                current_dial = 0 + (current_dial - 100)
            if current_dial == 0:
                zeros += 1


# for input in directions:
#     turn()

with open("input.txt", 'r') as file:
    for line in file:
        turn(line)

print("Total Zeros: " + str(zeros))
